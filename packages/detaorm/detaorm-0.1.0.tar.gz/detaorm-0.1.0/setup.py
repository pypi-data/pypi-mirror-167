# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['detaorm']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'detaorm',
    'version': '0.1.0',
    'description': 'An async ORM for DetaBase.',
    'long_description': '# DetaORM\n An async ORM for DetaBase.\n',
    'author': 'CircuitSacul',
    'author_email': 'circuitsacul@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
