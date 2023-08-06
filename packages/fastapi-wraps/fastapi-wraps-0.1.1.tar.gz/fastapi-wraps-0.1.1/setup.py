# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_wraps']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.83.0,<0.84.0']

setup_kwargs = {
    'name': 'fastapi-wraps',
    'version': '0.1.1',
    'description': '',
    'long_description': '# fastapi-wraps\n',
    'author': 'Paweł Rubin',
    'author_email': 'pawelrubindev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/pawelrubin/fastapi-wraps',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
