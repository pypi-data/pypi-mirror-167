# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scripts_json']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['scripts-json = scripts_json.main:main']}

setup_kwargs = {
    'name': 'scripts-json',
    'version': '1.0.4',
    'description': 'A tool to run scripts from a JSON file',
    'long_description': '# Scripts.json\n\nA tool to run scripts from a JSON file\n\n## Installation\n```\npip install scripts-json\n```\n\n## Usage\n\n```\nscripts-json [-h] [--file FILE] script\n```\n',
    'author': 'Olivier Audet-Yang',
    'author_email': 'oaudetyang@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/oliveman01/scripts.json',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
