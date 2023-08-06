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
    'version': '0.1.3',
    'description': '',
    'long_description': '# fastapi-wraps\n\n\n## Installation\n\n```shell\npip install fastapi-wraps\n```\n\n## Example\n\n```python\ndef save_request(\n    endpoint: Callable[P, Awaitable[RT]],\n) -> Callable[P, Awaitable[RT]]:\n    @fastapi_wraps(endpoint)\n    async def wrapper(\n        *args: Any,\n        __request: Request = Depends(get_request),\n        __db: Db = Depends(get_db),\n        **kwargs: Any,\n    ) -> RT:\n        __db.save(__request)\n        response = await endpoint(*args, **kwargs)\n        return response\n\n    return wrapper\n\n\napp = FastAPI()\n\n\n@app.get("/")\n@save_request\nasync def hello() -> str:\n    return "hello"\n```\n\n## Why?\n\nTo use dependencies provided by FastAPI\'s DI framework all dependencies have to be declared in the signature of the endpoint.\nHence, the decorator cannot simply use `functools.wraps`, as `functools.wraps` maintains the signature of the wrapped function. The `fastapi_wraps` decorator takes updates the resulting signature by merging parameters from the `wrapper` and the `wrapped` function.\n',
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
