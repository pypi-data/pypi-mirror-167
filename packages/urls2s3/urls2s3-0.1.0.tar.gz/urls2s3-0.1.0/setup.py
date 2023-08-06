# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['urls2s3']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.61,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.5.1,<13.0.0']

setup_kwargs = {
    'name': 'urls2s3',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'lemerchand',
    'author_email': 'phoenix.scooter@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
