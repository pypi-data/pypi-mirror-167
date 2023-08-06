# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['volosti']

package_data = \
{'': ['*']}

extras_require = \
{'all': ['aiosqlite>=0.17.0',
         'asyncpg>=0.26.0',
         'cryptography>=37.0.4,<38.0.0',
         'gunicorn>=20.1.0,<21.0.0',
         'hypercorn>=0.13.2',
         'jinja2>=3.1.2,<4.0.0',
         'pycryptodome>=3.15.0,<4.0.0',
         'python-multipart',
         'uvicorn>=0.18.2',
         'volosti-gui-kivy>=0,<1',
         'volosti-server-sanic>=0,<1',
         'volosti-server-starlette>=0,<1'],
 'gui-kivy': ['volosti-gui-kivy>=0,<1'],
 'gunicorn': ['gunicorn>=20.1.0,<21.0.0'],
 'hypercorn': ['hypercorn>=0.13.2'],
 'openssl': ['cryptography>=37.0.4,<38.0.0'],
 'postgresql': ['asyncpg>=0.26.0'],
 'pycryptodome': ['pycryptodome>=3.15.0,<4.0.0'],
 'server-sanic': ['volosti-server-sanic>=0,<1'],
 'server-sanic-wui': ['jinja2>=3.1.2,<4.0.0', 'volosti-server-sanic>=0,<1'],
 'server-starlette': ['volosti-server-starlette>=0,<1'],
 'server-starlette-wui': ['jinja2>=3.1.2,<4.0.0',
                          'python-multipart',
                          'volosti-server-starlette>=0,<1'],
 'sqlite': ['aiosqlite>=0.17.0'],
 'uvicorn': ['uvicorn>=0.18.2']}

setup_kwargs = {
    'name': 'volosti',
    'version': '0.1.dev2',
    'description': 'Метапакет разрабатываемого проекта',
    'long_description': '#######\nВолости\n#######\nМетапакет разрабатываемого проекта\n',
    'author': 'Ruslan Ilyasovich Gilfanov',
    'author_email': 'ri.gilfanov@yandex.ru',
    'maintainer': 'Ruslan Ilyasovich Gilfanov',
    'maintainer_email': 'ri.gilfanov@yandex.ru',
    'url': 'https://pypi.org/project/volosti',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
