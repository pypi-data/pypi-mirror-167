# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyasx', 'pyasx.data']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'python-dateutil>=2.8.2,<3.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pyasx',
    'version': '3.0.0',
    'description': 'Python library to pull data from ASX.com.au',
    'long_description': None,
    'author': 'JohnVonNeumann',
    'author_email': '18162779+JohnVonNeumann@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
