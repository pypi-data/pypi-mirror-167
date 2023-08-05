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
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Olivier Audet-Yang',
    'author_email': 'oaudetyang@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
