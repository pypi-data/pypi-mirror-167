# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_wraps']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fastapi-wraps',
    'version': '0.0.1',
    'description': '',
    'long_description': '# fastapi-wraps\n',
    'author': 'Paweł Rubin',
    'author_email': 'pawelrubindev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/pawelrubin/fastapi-wraps',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
