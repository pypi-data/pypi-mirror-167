# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fuk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fuk',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Pritam Soni',
    'author_email': 'pritam@grid.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
