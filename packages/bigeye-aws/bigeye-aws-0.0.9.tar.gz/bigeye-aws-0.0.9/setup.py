# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bigeye_aws', 'bigeye_aws.functions']

package_data = \
{'': ['*']}

install_requires = \
['bigeye-sdk>=0.4.0,<0.5.0', 'boto3>=1.19.9,<2.0.0']

setup_kwargs = {
    'name': 'bigeye-aws',
    'version': '0.0.9',
    'description': 'AWS functions and utilities for Bigeye.',
    'long_description': '# Bigeye AWS Library\nContains common utilities to interface with AWS.',
    'author': 'Bigeye',
    'author_email': 'support@bigeye.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
