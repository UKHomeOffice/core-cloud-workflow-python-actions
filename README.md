# core-cloud-workflow-python-actions

This repository contains actions for a full Python workflows

- `Python setup` - to set up python
- `Python lint` - to lint python code
- `Python format` - to format python code
- `Python test` - to test python code
- `Python upload` - to upload python code to a lambda

There are also two workflows that combine several of actions into self contained workflows

- `validation` - will lint, format, and test python code
- `build-publish` - will validate and then upload the python code to a aws lambda

## Pre-requisites

- Valid `python version` python version when running the validation workflow
- Valid `ROLE_TO_ASSUME` and `LAMBDA_ROLE_ARN`for uploading the python to lambda

## Usage

Workflows can be used as

```yml

jobs:
  validate:
    uses: UKHomeOffice/core-cloud-workflow-python-actions/.github/workflows/validation.yml@main
    with:
      working_directory: "hello-world"
      python_version: "3.14"

  upload:
    needs: validate
    uses: UKHomeOffice/core-cloud-workflow-python-actions/.github/workflows/upload.yml@main
    with:
      working_directory: "hello-world"
      python_version: "3.14"
      function_name: "hello-world"
      python_runtime: "python3.14"
      handler: "lambda_function.lambda_handler"
    secrets:
      ROLE_TO_ASSUME: ${{ secrets.ROLE_TO_ASSUME }}
      LAMBDA_ROLE_ARN: ${{ secrets.LAMBDA_ROLE_ARN }}
```

The actions can be used in similar manner as well