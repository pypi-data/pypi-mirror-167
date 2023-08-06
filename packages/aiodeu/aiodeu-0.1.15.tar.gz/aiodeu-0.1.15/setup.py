# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiodeu']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['aiodeu = aiodeu.console:main']}

setup_kwargs = {
    'name': 'aiodeu',
    'version': '0.1.15',
    'description': 'aio data engineering utils',
    'long_description': None,
    'author': 'Josh Rowe',
    'author_email': 's-block@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/s-block/aiodeu',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
