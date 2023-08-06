# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_rabbitmq']

package_data = \
{'': ['*']}

install_requires = \
['pika>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'python-rabbitmq',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Huynh Doan Thinh',
    'author_email': 'hdthinh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
