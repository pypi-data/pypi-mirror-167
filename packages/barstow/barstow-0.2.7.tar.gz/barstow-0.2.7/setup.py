# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['barstow']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.1', 'pyarrow>=9.0.0,<10.0.0']

setup_kwargs = {
    'name': 'barstow',
    'version': '0.2.7',
    'description': 'Library for managing Arrow datasets',
    'long_description': None,
    'author': 'Mat Leonard',
    'author_email': 'leonard.mat@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4',
}


setup(**setup_kwargs)
