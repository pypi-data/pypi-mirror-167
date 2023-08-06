# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['volosti_server_starlette', 'volosti_server_starlette.wui']

package_data = \
{'': ['*']}

install_requires = \
['starlette>=0.20.4', 'volosti-server-common>=0.1.dev1,<0.1']

extras_require = \
{'all': ['aiosqlite>=0.17.0',
         'asyncpg>=0.26.0',
         'cryptography>=37.0.4,<38.0.0',
         'gunicorn>=20.1.0,<21.0.0',
         'hypercorn>=0.13.2',
         'jinja2>=3.1.2,<4.0.0',
         'pycryptodome>=3.15.0,<4.0.0',
         'python-multipart',
         'uvicorn>=0.18.2'],
 'gunicorn': ['gunicorn>=20.1.0,<21.0.0'],
 'hypercorn': ['hypercorn>=0.13.2'],
 'openssl': ['cryptography>=37.0.4,<38.0.0'],
 'postgresql': ['asyncpg>=0.26.0'],
 'pycryptodome': ['pycryptodome>=3.15.0,<4.0.0'],
 'sqlite': ['aiosqlite>=0.17.0'],
 'uvicorn': ['uvicorn>=0.18.2'],
 'wui': ['jinja2>=3.1.2,<4.0.0', 'python-multipart']}

setup_kwargs = {
    'name': 'volosti-server-starlette',
    'version': '0.1.dev1',
    'description': 'Разрабатываемая реализация сервера Волостей на веб-фреймворке Starlette',
    'long_description': 'volosti-server-starlette\n========================\nРазрабатываемая реализация сервера Волостей на веб-фреймворке Starlette\n',
    'author': 'Ruslan Ilyasovich Gilfanov',
    'author_email': 'ri.gilfanov@yandex.ru',
    'maintainer': 'Ruslan Ilyasovich Gilfanov',
    'maintainer_email': 'ri.gilfanov@yandex.ru',
    'url': 'https://pypi.org/project/volosti-server-starlette',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
