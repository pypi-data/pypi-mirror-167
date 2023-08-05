# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['click_prompt']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4', 'questionary>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'click-prompt',
    'version': '0.5.1',
    'description': 'click-prompt provides more beautiful interactive options for the Python click library',
    'long_description': "# click-prompt \n\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/click-prompt)](https://pypi.org/project/click-prompt/) \n[![PyPI version](https://img.shields.io/pypi/v/click-prompt)](https://pypi.org/project/click-prompt/) \n\n\nclick-prompt provides more beautiful interactive options for the Python click\nlibrary. The library is inspired by a post on [stackoverflow.com](https://stackoverflow.com/questions/54311067/)\n\n## Usage\n\nThe library can be used in two ways: 1) as decorator, or 2) as type parameter.\n\n### With decorators\n\n\n```python\nimport click\nfrom click_prompt import choice_option\n\n@click.command()\n@choice_option('--fruit', type=click.Choice(['Apples', 'Bananas', 'Grapefruits', 'Mangoes']))\ndef select_fruit(fruit: str):\n    print(fruit)\n```\n\n### As class\n\n```python\nimport click\nfrom click_prompt import ChoiceOption\n\n@click.command()\n@click.option('--fruit', \n              type=click.Choice(['Apples', 'Bananas', 'Grapefruits', 'Mangoes']),\n              cls=ChoiceOption)\ndef select_fruit(fruit: str):\n    print(fruit)\n```\n\n## Example\n\n![Example](./docs/example_cli.gif)\n\n\n## Available Decorators\n\nHere is a list of available decorators that can be used with the click library\ninstead of a `click.Option` decorator\n\n - `choice_option`: Select a single item out of a list. Use the parameter\n   `multiple=True` to select multiple items out of a list\n - `confirm_option`: Yes/No confirmation\n - `filepath_option`: Select a file path with auto completion\n - `auto_complete_option`: Auto completion given a list\n\nfor every `click.Option` there is also a `click.Argument` implementation\n",
    'author': 'Markus Grotz',
    'author_email': 'grotz@uw.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.9,<4.0',
}


setup(**setup_kwargs)
