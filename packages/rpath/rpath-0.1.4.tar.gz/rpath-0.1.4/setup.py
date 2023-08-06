# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpath']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rpath',
    'version': '0.1.4',
    'description': "R's path handling functions for Python",
    'long_description': None,
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
