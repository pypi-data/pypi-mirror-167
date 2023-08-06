# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sigsum']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sigsum',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'Grégoire Détrez',
    'author_email': 'gregoire@mullvad.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
