"""Build Process
"""
import sys
import os
import re
import copy
import json
import yaml
import openapi_spec_validator
import jsonpath_ng
import inspect

try:
    from typing import Union, Dict, Literal
except ImportError:
    from typing_extensions import Literal


class Bundler(object):
    """Bundles OpenAPI yaml files into a single API document

    Notes
    -----
    - Bundles multiple OpenAPI v3.x yaml files into a single file.
    - Does not inline schemas indicated by ref keywords but normalizes them by
      removing the file path.
    - Validates the bundled file

    Args
    ----
        output_dir (str): The directory where files will be output
        api_files (str): The top level api files
    """

    class description(str):
        pass

    @staticmethod
    def literal_representer(dumper, data):
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style="|"
        )

    def __init__(self, api_files, output_dir="./"):
        self._parsers = {}
        self._api_files = api_files
        self._output_dir = os.path.abspath(output_dir)
        if os.path.exists(self._output_dir) is False:
            os.makedirs(self._output_dir)
        self.__python = os.path.normpath(sys.executable)
        self._content = {}
        self._includes = {}
        self._resolved = []
        self._errors = []
        yaml.add_representer(Bundler.description, Bundler.literal_representer)

    def _get_parser(self, pattern):
        if pattern not in self._parsers:
            parser = jsonpath_ng.parse(pattern)
            self._parsers[pattern] = parser
        else:
            parser = self._parsers[pattern]
        return parser

    @property
    def openapi_filepath(self):
        return self._output_filename

    def bundle(self):
        self._errors = []
        self._output_filename = os.path.join(self._output_dir, "openapi.yaml")
        self._json_filename = os.path.join(self._output_dir, "openapi.json")
        self._content = {}
        self._includes = {}
        self._resolved = []
        for api_filename in self._api_files:
            api_filename = os.path.normpath(os.path.abspath(api_filename))
            self._base_dir = os.path.dirname(api_filename)
            self._api_filename = os.path.basename(api_filename)
            self._read_file(self._base_dir, self._api_filename)
        self._resolve_x_include()
        self._resolve_x_pattern("x-field-pattern")
        self._resolve_x_constraint()
        self._resolve_x_status()
        self._remove_x_include()
        self._resolve_license()
        self._validate_required_responses()
        self._resolve_strings(self._content)
        self._resolve_keys(self._content)
        self._validate_errors()
        with open(self._output_filename, "w") as fp:
            yaml.dump(
                self._content,
                fp,
                indent=2,
                allow_unicode=True,
                line_break="\n",
                sort_keys=False,
            )
        with open(self._json_filename, "w") as fp:
            fp.write(json.dumps(self._content, indent=4))
        self._validate_file()

    def _validate_errors(self):
        if len(self._errors) > 0:
            raise TypeError("\n".join(self._errors))

    def _validate_required_responses(self):
        """Ensure all paths include a 400 and 500 response.

        Print every path that does not include a 400 or 500 response.

        Returns
        -------
        Exception: one or more paths is missing a 400 or 500 response
        None: all paths have a 400 and 500 response
        """
        responses = self._get_parser("$..paths..responses").find(self._content)
        required_error_codes = ["400", "500"]
        missing_paths = ""
        for response in responses:
            missing = set(required_error_codes).difference(
                set(response.value.keys())
            )
            if len(missing):
                error_message = "{}: is missing the following required responses: {}".format(
                    response.full_path,
                    missing,
                )
                print(error_message)
                missing_paths += "{}\n".format(error_message)
        if len(missing_paths) > 0:
            raise Exception(missing_paths)
        return None

    def _validate_file(self):
        print("validating {}...".format(self._output_filename))
        with open(self._output_filename) as fid:
            yobject = yaml.safe_load(fid)
            openapi_spec_validator.validate_v3_spec(yobject)
        print("validating complete")

    def _read_file(self, base_dir, filename):
        filename = os.path.join(base_dir, filename)
        filename = os.path.abspath(os.path.normpath(filename))
        base_dir = os.path.dirname(filename)
        with open(filename) as fid:
            yobject = yaml.safe_load(fid)
        self._process_yaml_object(base_dir, yobject)

    def _process_yaml_object(self, base_dir, yobject):
        for key, value in yobject.items():
            if (
                key in ["openapi", "info", "servers"]
                and key not in self._content.keys()
            ):
                self._content[key] = value
            elif key in ["paths"]:
                if key not in self._content.keys():
                    self._content[key] = {}
                for sub_key in value.keys():
                    self._content[key][sub_key] = value[sub_key]
            elif key == "components":
                if key not in self._content.keys():
                    self._content[key] = {"responses": {}, "schemas": {}}
                self._validate_names("^[+a-zA-Z0-9_]+$", "schemas", value)
                self._validate_names("^[+a-zA-Z0-9_]+$", "responses", value)
                self._check_nested_components(value)
        self._resolve_refs(base_dir, yobject)

    def _validate_names(self, regex, components_key, components):
        if components_key not in components:
            return
        objects = components[components_key]
        for key, value in objects.items():
            if "properties" in objects[key]:
                for name in objects[key]["properties"]:
                    if re.match(regex, name) is None:
                        raise NameError(
                            "%s property name `%s` contains invalid characters"
                            % (key, name)
                        )
            self._content["components"][components_key][key] = value

    def _check_nested_components(self, components):
        objects = components["schemas"]
        errors = []
        for component_name, component_value in objects.items():
            if "properties" in component_value:
                component_properties = component_value["properties"]
                for property_name in component_properties:
                    property_obj = component_properties[property_name]
                    if "type" in property_obj:
                        proprty_type = property_obj["type"]
                        if proprty_type == "object":
                            errors.append(
                                "\n*** Unsupported. Property '{}'.'{}' is a nested component ***".format(
                                    component_name,
                                    property_name,
                                )
                            )
        if len(errors) > 0:
            raise TypeError("".join(errors))

    def _resolve_refs(self, base_dir, yobject):
        """Resolving references is relative to the current file location"""
        if isinstance(yobject, dict):
            for key, value in yobject.items():
                if key == "$ref" and value.startswith("#") is False:
                    refs = value.split("#")
                    if refs[1] not in self._resolved:
                        self._resolved.append(refs[1])
                        print("resolving %s" % value)
                        self._read_file(base_dir, refs[0])
                    yobject[key] = "#%s" % refs[1]
                elif isinstance(value, str) and "x-inline" in value:
                    refs = value.split("#")
                    print("inlining %s" % value)
                    inline = self._get_inline_ref(base_dir, refs[0], refs[1])
                    yobject[key] = inline
                elif key == "x-include":
                    for include_ref in value:
                        if include_ref not in self._includes:
                            include = self._get_schema_object(
                                base_dir, include_ref
                            )
                            self._resolve_refs(base_dir, include)
                            self._includes[include_ref] = include
                else:
                    self._length_restriction(value)
                    self._required_restriction(key, value)
                    self._resolve_refs(base_dir, value)
        elif isinstance(yobject, list):
            for item in yobject:
                self._resolve_refs(base_dir, item)

    def _length_restriction(self, value):
        restricted_keys = {
            "length",
            "minimum",
            "maximum",
            "minLength",
            "maxLength",
        }
        if isinstance(value, dict):
            intersect_keys = restricted_keys.intersection(set(value.keys()))
            if (
                len(intersect_keys) > 0
                and "format" in value.keys()
                and value["format"] in ["ipv4", "ipv6", "mac"]
            ):
                stacks = inspect.stack()
                property = "{}/{}/{}".format(
                    stacks[3].frame.f_locals["key"]
                    if "key" in stacks[3].frame.f_locals
                    else "",
                    stacks[2].frame.f_locals["key"]
                    if "key" in stacks[2].frame.f_locals
                    else "",
                    stacks[1].frame.f_locals["key"],
                )
                self._errors.append(
                    "Property {property} should not contain {keys} with format {format}".format(
                        property=property,
                        keys=intersect_keys,
                        format=value["format"],
                    )
                )

    def _required_restriction(self, schema_name, value):
        expected_set = {"required", "properties"}
        if isinstance(value, dict) and expected_set.issubset(value.keys()):
            if isinstance(value["required"], list):
                for required in value["required"]:
                    if "default" in value["properties"][required].keys():
                        self._errors.append(
                            "Property {property} within schema {name} have "
                            "both required as well as default".format(
                                property=required, name=schema_name
                            )
                        )

    def _resolve_x_pattern(self, pattern_extension):
        """Find all instances of pattern_extension in the openapi content
        and generate a #/components/schemas/... pattern schema object that is
        specific to the property hosting the pattern extension content.
        Replace the x-field-pattern schema with a $ref to the generated schema.
        """
        import jsonpath_ng

        for xpattern_path in self._get_parser(
            "$..{}".format(pattern_extension)
        ).find(self._content):
            print("generating %s..." % (str(xpattern_path.full_path)))
            object_name = xpattern_path.full_path.left.left.left.right.fields[
                0
            ]
            property_name = xpattern_path.full_path.left.right.fields[0]
            property_schema = jsonpath_ng.Parent().find(xpattern_path)[0].value
            xpattern = xpattern_path.value
            schema_name = "Pattern.{}.{}".format(
                "".join(
                    [
                        piece[0].upper() + piece[1:]
                        for piece in object_name.split("_")
                    ]
                ),
                "".join(
                    [
                        piece[0].upper() + piece[1:]
                        for piece in property_name.split("_")
                    ]
                ),
            )
            format = None
            type_name = xpattern["format"]
            if type_name in ["ipv4", "ipv6", "mac", "enum"]:
                format = type_name
                type_name = "string"
            description = "TBD"
            if "description" in xpattern:
                description = xpattern["description"]
            elif "description" in property_schema:
                description = property_schema["description"]

            if xpattern["format"] == "checksum":
                self._generate_checksum_schema(
                    xpattern, schema_name, description
                )
            else:
                self._generate_value_schema(
                    xpattern, schema_name, description, type_name, format
                )

            property_schema["$ref"] = "#/components/schemas/{}".format(
                schema_name
            )
            del property_schema[pattern_extension]

    def _generate_checksum_schema(self, xpattern, schema_name, description):
        """Generate a checksum schema object"""
        schema = {
            "description": description,
            "type": "object",
            "properties": {
                "choice": {
                    "description": "The type of checksum",
                    "type": "string",
                    "enum": ["generated", "custom"],
                    "default": "generated",
                },
                "generated": {
                    "description": "A system generated checksum value",
                    "type": "string",
                    "enum": ["good", "bad"],
                    "default": "good",
                },
                "custom": {
                    "description": "A custom checksum value",
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 2 ** int(xpattern.get("length", 8)) - 1,
                },
            },
        }
        self._content["components"]["schemas"][schema_name] = schema

    def _generate_value_schema(
        self, xpattern, schema_name, description, type_name, format
    ):
        xconstants = (
            xpattern["x-constants"] if "x-constants" in xpattern else None
        )
        schema = {
            "description": description,
            "type": "object",
            "properties": {
                "choice": {
                    "type": "string",
                    "enum": ["value", "values"],
                    "default": "value",
                },
                "value": {"type": copy.deepcopy(type_name)},
                "values": {
                    "type": "array",
                    "items": {"type": copy.deepcopy(type_name)},
                },
            },
        }
        if xconstants is not None:
            schema["x-constants"] = copy.deepcopy(xconstants)
        if "features" in xpattern:
            if "auto" in xpattern["features"]:
                if "default" not in xpattern:
                    self._errors.append(
                        "default must be set for property {}, when auto feature is enabled".format(
                            schema_name
                        )
                    )
                schema["properties"]["choice"]["enum"].append("auto")
                schema["properties"]["choice"]["default"] = "auto"
                description = [
                    "The OTG implementation can provide a system generated",
                    "value for this property. If the OTG is unable to generate a value",
                    "the default value must be used.",
                ]
                schema["properties"]["auto"] = {
                    "description": "\n".join(description),
                    "type": copy.deepcopy(type_name),
                }
                self._apply_common_x_field_pattern_properties(
                    schema["properties"]["auto"],
                    xpattern,
                    format,
                    property_name="auto",
                )
            if "metric_group" in xpattern["features"]:
                schema["properties"]["metric_group"] = {
                    "description": """A unique name is used to indicate to the system that the field may """
                    """extend the metric row key and create an aggregate metric row for """
                    """every unique value. """
                    """To have metric group columns appear in the flow metric rows the flow """
                    """metric request allows for the metric_group value to be specified """
                    """as part of the request.""",
                    "type": "string",
                }
        if "enums" in xpattern:
            schema["properties"]["value"]["enum"] = copy.deepcopy(
                xpattern["enums"]
            )
            schema["properties"]["values"]["items"]["enum"] = copy.deepcopy(
                xpattern["enums"]
            )
        if xpattern["format"] in ["integer", "ipv4", "ipv6", "mac"]:
            counter_pattern_name = "{}.Counter".format(schema_name)
            schema["properties"]["choice"]["enum"].extend(
                ["increment", "decrement"]
            )
            schema["properties"]["increment"] = {
                "$ref": "#/components/schemas/{}".format(counter_pattern_name)
            }
            schema["properties"]["decrement"] = {
                "$ref": "#/components/schemas/{}".format(counter_pattern_name)
            }
            counter_schema = {
                "description": "{} counter pattern".format(xpattern["format"]),
                "type": "object",
                "properties": {
                    "start": {"type": type_name},
                    "step": {"type": type_name},
                },
            }
            if "features" in xpattern and "count" in xpattern["features"]:
                counter_schema["properties"]["count"] = {
                    "type": "integer",
                    "default": 1,
                }
            self._apply_common_x_field_pattern_properties(
                counter_schema["properties"]["start"],
                xpattern,
                format,
                property_name="start",
            )
            self._apply_common_x_field_pattern_properties(
                counter_schema["properties"]["step"],
                xpattern,
                format,
                property_name="step",
            )
            if xconstants is not None:
                counter_schema["x-constants"] = copy.deepcopy(xconstants)
            self._content["components"]["schemas"][
                counter_pattern_name
            ] = counter_schema
        self._apply_common_x_field_pattern_properties(
            schema["properties"]["value"],
            xpattern,
            format,
            property_name="value",
        )
        self._apply_common_x_field_pattern_properties(
            schema["properties"]["values"],
            xpattern,
            format,
            property_name="values",
        )
        self._content["components"]["schemas"][schema_name] = schema

    def _apply_common_x_field_pattern_properties(
        self, schema, xpattern, format, property_name
    ):
        # type: (Dict, Dict, str, Union[Literal["start"], Literal["step"], Literal["value"], Literal["values"]])
        step_defaults = {
            "mac": "00:00:00:00:00:01",
            "ipv4": "0.0.0.1",
            "ipv6": "::1",
        }
        if "default" in xpattern:
            schema["default"] = xpattern["default"]
            if property_name == "step":
                if format in step_defaults:
                    schema["default"] = step_defaults[format]
                else:
                    schema["default"] = 1
            elif property_name == "values":
                schema["default"] = [schema["default"]]
        if format is not None:
            schema["format"] = format
        if "length" in xpattern:
            schema["minimum"] = 0
            schema["maximum"] = 2 ** int(xpattern["length"]) - 1

    def _resolve_x_include(self):
        """Find all instances of x-include in the openapi content
        and merge the x-include content into the parent object
        Remove the x-include and the included content
        """
        include_schemas = []
        for xincludes in self._get_parser("$..x-include").find(self._content):
            parent_schema_object = (
                jsonpath_ng.Parent().find(xincludes)[0].value
            )
            for xinclude in xincludes.value:
                print("resolving %s..." % (str(xinclude)))
                include_schemas.append(xinclude)
                include_schema_object = self._includes[xinclude]
                self._merge(
                    copy.deepcopy(include_schema_object), parent_schema_object
                )
            del parent_schema_object["x-include"]

    def _remove_x_include(self):
        refs = self._get_parser('$.."$ref"').find(self._content)
        for item in set(self._includes):
            pieces = item.split("#/")[1].split("/")
            value = "#/{}".format("/".join(pieces))
            match = False
            for ref in refs:
                if ref.value == value:
                    match = True
                    break
            if match is False:
                content = self._content
                for piece in pieces[0:-1]:
                    content = content[piece]
                if pieces[-1] in content:
                    del content[pieces[-1]]

    def _resolve_x_status(self):
        """Find all instances of x-constraint in the openapi content
        and merge the x-constraint content into the parent object description
        """
        import jsonpath_ng

        for xstatus in self._get_parser("$..x-status").find(self._content):
            if xstatus.value == "current":
                continue
            print("resolving %s..." % (str(xstatus.full_path)))
            parent_schema_object = jsonpath_ng.Parent().find(xstatus)[0].value
            if "description" not in parent_schema_object:
                parent_schema_object["description"] = "TBD"
            parent_schema_object[
                "description"
            ] = "Status: {status}\n{description}".format(
                status=xstatus.value,
                description=parent_schema_object["description"],
            )

    def _resolve_x_constraint(self):
        """Find all instances of x-constraint in the openapi content
        and merge the x-constraint content into the parent object description
        """
        import jsonpath_ng

        for xconstraint in self._get_parser("$..x-constraint").find(
            self._content
        ):
            print("resolving %s..." % (str(xconstraint.full_path)))
            parent_schema_object = (
                jsonpath_ng.Parent().find(xconstraint)[0].value
            )
            if "description" not in parent_schema_object:
                parent_schema_object["description"] = "TBD"
            parent_schema_object["description"] += "\n\nx-constraint:\n"
            for constraint in xconstraint.value:
                parent_schema_object["description"] += "- {}\n".format(
                    constraint
                )

    def _merge(self, src, dst):
        """
        Recursively update a dict.
        Subdict's won't be overwritten but also updated.
        """
        for key, value in src.items():
            if key not in dst:
                dst[key] = value
            elif isinstance(value, list):
                for item in value:
                    if item not in dst[key]:
                        dst[key].append(item)
            elif isinstance(value, dict):
                self._merge(value, dst[key])
            elif key == "description":
                dst[key] = "{}\n{}".format(dst[key], value)
        return dst

    def _get_schema_object(self, base_dir, schema_path):

        json_path = "$..'%s'" % schema_path.split("/")[-1]
        schema_object = self._get_parser(json_path).find(self._content)
        if len(schema_object) == 0:
            schema_object = self._get_schema_object_from_file(
                base_dir, schema_path
            )
        else:
            schema_object = schema_object[0].value
        return schema_object

    def _get_schema_object_from_file(self, base_dir, schema_path):
        import yaml

        paths = schema_path.split("#")
        filename = os.path.join(base_dir, paths[0])
        filename = os.path.abspath(os.path.normpath(filename))
        with open(filename) as fid:
            schema_file = yaml.safe_load(fid)
        json_path = "$..'%s'" % schema_path.split("/")[-1]
        schema_object = self._get_parser(json_path).find(schema_file)[0].value
        return schema_object

    def _resolve_strings(self, content):
        """Fix up strings"""
        for key, value in content.items():
            if isinstance(value, dict):
                self._resolve_strings(value)
            elif key == "description":
                descr = copy.deepcopy(value)
                content[key] = Bundler.description(descr)

    def _resolve_license(self):
        """License object is not required by the OpenAPI spec.
        If the license object is provided then name is a required property.
        """
        if "license" not in self._content["info"]:
            self._content["info"]["license"] = {"name": "NO-LICENSE-PRESENT"}
        elif "name" not in self._content["info"]["license"]:
            raise Exception(
                "The following properties are REQUIRED: license.name"
            )

    def _resolve_keys(self, content):
        changes = {}
        for key, value in content.items():
            if isinstance(key, int):
                changes[key] = value
            if isinstance(value, dict):
                self._resolve_keys(value)
        for key, value in changes.items():
            content[str(key)] = value
            del content[key]


if __name__ == "__main__":
    Bundler(api_files=["./tests/api/api.yaml"]).bundle()
