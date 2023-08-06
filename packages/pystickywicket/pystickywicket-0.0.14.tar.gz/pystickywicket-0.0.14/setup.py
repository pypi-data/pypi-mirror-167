# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pystickywicket']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=4.0.1,<5.0.0',
 'mkdocs-material>=8.2.11,<9.0.0',
 'mkdocs>=1.3.0,<2.0.0',
 'mkdocstrings>=0.18.1,<0.19.0',
 'mock>=4.0.3,<5.0.0',
 'poetry-dynamic-versioning>=0.14.1,<0.15.0',
 'pytest-cov>=3.0.0,<4.0.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'pystickywicket',
    'version': '0.0.14',
    'description': 'A python library for interacting with the API provided by the national cricket board of England and Wales',
    'long_description': 'None',
    'author': 'Matthew Macdonald-Wallace',
    'author_email': 'matt@doics.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
