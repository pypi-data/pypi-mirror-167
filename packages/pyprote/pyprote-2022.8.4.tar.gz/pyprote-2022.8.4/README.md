# pyprote: A Python package for creating Templates for python projects

## Installation from PyPi

```shell
pip install pyprote
```
For **test**-PyPi dev version:

```shell
pip install -i https://test.pypi.org/simple/ pyprote
```

# Usage

## Create a new project

### Get default template:
```shell
pyprote
```

You will have to replace all instances of `PY_PRO_TE_FILL_ME_IN` with your own project name, email etc..


### Fill the template cli arguments:
```shell
pyprote --package_name my_cool_package_name \
        --package_version 0.1.0 \
        --package_description 'My cool package description' \
        --package_author_name 'John Doe' \
        --package_author_email john@doe \
        --package_link https://cool.package \
        --out_dir pyprote_output_dir
```


# Installation - development

Create a virtual environment.

## Poetry:
```shell
poetry install
```

# Testing

Running the tests requires to run the following command in the root folder (of course in the virtual environment):

```shell
poetry run pytest
```


# CLI app

```shell
pyprote --help
```

# Formatting

```shell
poetry run black . && \
poetry run isort . && \
poetry run flake8 . && \
poetry run mypy .
```

## Versioning

Update (calendar) version with [bumpver](https://github.com/mbarkhau/bumpver):

```shell
poetry run bumpver update --dry --patch
```
`--dry` just shows how the version WOULD change.
```shell
poetry run bumpver update --patch
```


## How to build a Python package?

To build the package, you need to go to the root folder of the package and run the following command:

```shell
poetry build
```

The built package is now located in the dist/ folder.


## Publishing your package in PyPi

Publishing is done automatically using GitHub actions.

Commit to master creates test-pypi release.

Tagged Commit creates real pypi release.
