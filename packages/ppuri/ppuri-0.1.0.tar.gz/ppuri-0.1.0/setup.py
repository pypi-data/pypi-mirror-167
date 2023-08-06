# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ppuri', 'ppuri.component', 'ppuri.scheme']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'pyparsing>=3.0.9,<4.0.0']

setup_kwargs = {
    'name': 'ppuri',
    'version': '0.1.0',
    'description': 'A pyparsing based URI parser/scanner',
    'long_description': None,
    'author': 'Simon Kennedy',
    'author_email': 'sffjunkie+code@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
