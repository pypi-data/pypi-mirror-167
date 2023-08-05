# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['comfig']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.6.1,<0.7.0']

setup_kwargs = {
    'name': 'comfig',
    'version': '0.2.2',
    'description': '',
    'long_description': None,
    'author': 'Stanislav Zmiev',
    'author_email': 'szmiev2000@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
