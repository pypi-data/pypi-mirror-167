# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['volosti_common']

package_data = \
{'': ['*']}

install_requires = \
['argon2-cffi>=21.3.0,<22.0.0',
 'babel>=2.10.3,<3.0.0',
 'httpx>=0.23.0',
 'marshmallow>=3.18.0,<4.0.0',
 'passlib>=1.7.4,<2.0.0']

extras_require = \
{'openssl': ['cryptography>=37.0.4,<38.0.0'],
 'pycryptodome': ['pycryptodome>=3.15.0,<4.0.0']}

setup_kwargs = {
    'name': 'volosti-common',
    'version': '0.1.dev0',
    'description': 'Общий исходный код реализаций Волостей',
    'long_description': 'volosti-common\n==============\nОбщий исходный код реализаций Волостей.\n',
    'author': 'Ruslan Ilyasovich Gilfanov',
    'author_email': 'ri.gilfanov@yandex.ru',
    'maintainer': 'Ruslan Ilyasovich Gilfanov',
    'maintainer_email': 'ri.gilfanov@yandex.ru',
    'url': 'https://pypi.org/project/volosti-common',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
