import json
import os
import pprint
import re

from jsonschema import Draft7Validator

def json_from_file(file_path):
    with open(file_path) as f:
        return json.load(f)


def validate_file(json_schema, path_pattern, file_path):
    pattern = re.compile(path_pattern)
    if pattern.match(file_path):
        print('validating {}'.format(file_path))
        schema = json_from_file(json_schema)
        instance = json_from_file(file_path)

        validator = Draft7Validator(schema)
        return sorted(validator.iter_errors(instance), key=str)
    else:
        return []
