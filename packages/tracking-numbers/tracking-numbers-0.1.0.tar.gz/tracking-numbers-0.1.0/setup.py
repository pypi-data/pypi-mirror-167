# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tracking_numbers', 'tracking_numbers.helpers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tracking-numbers',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jonathan Como',
    'author_email': 'jonathan.como@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
