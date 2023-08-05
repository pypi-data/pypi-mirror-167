# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['normal_form']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0',
 'loguru>=0.6.0,<0.7.0',
 'more-itertools>=8.14.0,<9.0.0',
 'python-sat[aiger,pblib]>=0.1.7-dev.15,<0.2.0',
 'tqdm>=4.64.0,<5.0.0',
 'typing-extensions>=4.3.0,<5.0.0']

setup_kwargs = {
    'name': 'normal-form',
    'version': '0.1.0',
    'description': 'A Python package for working with Conjunctive Normal Form (CNFs) and Boolean Satisfiability',
    'long_description': 'None',
    'author': 'Vaibhav Karve',
    'author_email': 'vkarve@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
