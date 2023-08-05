# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['pyprote', 'pyprote.logging_config']

package_data = \
{'': ['*'],
 'pyprote': ['templates/*',
             'templates/package_name_template/*',
             'templates/package_name_template/logging_config_template/*',
             'templates/tests_template/*']}

entry_points = \
{'console_scripts': ['pyprote = pyprote.__main__:main']}

setup_kwargs = {
    'name': 'pyprote',
    'version': '2022.8.4',
    'description': 'A tool for creating python packages.',
    'long_description': "# pyprote: A Python package for creating Templates for python projects\n\n## Installation from PyPi\n\n```shell\npip install pyprote\n```\nFor **test**-PyPi dev version:\n\n```shell\npip install -i https://test.pypi.org/simple/ pyprote\n```\n\n# Usage\n\n## Create a new project\n\n### Get default template:\n```shell\npyprote\n```\n\nYou will have to replace all instances of `PY_PRO_TE_FILL_ME_IN` with your own project name, email etc..\n\n\n### Fill the template cli arguments:\n```shell\npyprote --package_name my_cool_package_name \\\n        --package_version 0.1.0 \\\n        --package_description 'My cool package description' \\\n        --package_author_name 'John Doe' \\\n        --package_author_email john@doe \\\n        --package_link https://cool.package \\\n        --out_dir pyprote_output_dir\n```\n\n\n# Installation - development\n\nCreate a virtual environment.\n\n## Poetry:\n```shell\npoetry install\n```\n\n# Testing\n\nRunning the tests requires to run the following command in the root folder (of course in the virtual environment):\n\n```shell\npoetry run pytest\n```\n\n\n# CLI app\n\n```shell\npyprote --help\n```\n\n# Formatting\n\n```shell\npoetry run black . && \\\npoetry run isort . && \\\npoetry run flake8 . && \\\npoetry run mypy .\n```\n\n## Versioning\n\nUpdate (calendar) version with [bumpver](https://github.com/mbarkhau/bumpver):\n\n```shell\npoetry run bumpver update --dry --patch\n```\n`--dry` just shows how the version WOULD change.\n```shell\npoetry run bumpver update --patch\n```\n\n\n## How to build a Python package?\n\nTo build the package, you need to go to the root folder of the package and run the following command:\n\n```shell\npoetry build\n```\n\nThe built package is now located in the dist/ folder.\n\n\n## Publishing your package in PyPi\n\nPublishing is done automatically using GitHub actions.\n\nCommit to master creates test-pypi release.\n\nTagged Commit creates real pypi release.\n",
    'author': 'Sebastian Cattes',
    'author_email': 'sebastian.cattes@inwt-statistics.de',
    'maintainer': 'Sebastian Cattes',
    'maintainer_email': 'sebastian.cattes@inwt-statistics.de',
    'url': 'https://github.com/Cattes/pypote',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10.0,<3.11',
}


setup(**setup_kwargs)
