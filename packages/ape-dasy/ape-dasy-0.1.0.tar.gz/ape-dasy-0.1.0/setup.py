# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ape_dasy']

package_data = \
{'': ['*']}

install_requires = \
['dasy==0.1.18', 'eth-ape>=0.5.1,<0.6.0']

setup_kwargs = {
    'name': 'ape-dasy',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'z80',
    'author_email': 'z80@ophy.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
