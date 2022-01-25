# JSON Schema Validator

A Github Action for validating JSON using specified JSON schema.

## How to use it?

Create `.github/workflows/<workflow_name>.yml`

```yaml
on:
  pull_request:
    branches:
      - master
  push:
    branches:
      - master
name: JSON validation workflow
jobs:
  validate_configurations:
    name: Validate configurations
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Validate BigQuery schema
        uses: snapcart/json-schema-validator@v1.0.0
        with:
          json_schema: ./schemas/bigquery_schema.schema
          json_path_pattern: .*bigquery_schema.json$
      - name: Validate other schema
        uses: snapcart/json-schema-validator@v1.0.0
        with:
          json_schema: ./schemas/other_schema.schema
          json_path_pattern: .*other_schema.json$
```

Inputs|Required|Default|Description
------|--------|-------|-----------
`json_schema`|Yes|-|Path to the JSON Schema to validate with
`json_path_pattern`|Yes|-|Path to JSON files in RegEx
