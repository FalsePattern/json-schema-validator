import json
import os
from pathlib import Path

from utils import (json_from_file, validate_file)

json_schema = os.getenv('INPUT_JSON_SCHEMA')
json_path_pattern = os.getenv('INPUT_JSON_PATH_PATTERN')

event_path = os.getenv('GITHUB_EVENT_PATH')

errors = []

for file in Path('.').rglob('*.json'):
    filename = "./" + str(file)
    validation_errors = validate_file(json_schema, json_path_pattern, filename)

    if len(validation_errors):
        errors.append({
            'path': filename,
            'errors': validation_errors
        })

if len(errors):

    for error in errors:
        print(error)

    raise Exception('Fail validation')
