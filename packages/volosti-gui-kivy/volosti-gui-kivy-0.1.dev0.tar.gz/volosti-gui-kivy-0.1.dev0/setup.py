# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['volosti_gui_kivy']

package_data = \
{'': ['*']}

install_requires = \
['kivy>=2.1.0,<3.0.0', 'volosti-common>=0.1.dev0,<0.1']

extras_require = \
{'all': ['cryptography>=37.0.4,<38.0.0', 'pycryptodome>=3.15.0,<4.0.0'],
 'openssl': ['cryptography>=37.0.4,<38.0.0'],
 'pycryptodome': ['pycryptodome>=3.15.0,<4.0.0']}

setup_kwargs = {
    'name': 'volosti-gui-kivy',
    'version': '0.1.dev0',
    'description': 'Реализация графического интерфейса пользователя Волостей на графическом фреймворке Kivy',
    'long_description': 'volosti-gui-kivy\n================\nРеализация графического интерфейса пользователя Волостей на графическом фреймворке Kivy.\n',
    'author': 'Ruslan Ilyasovich Gilfanov',
    'author_email': 'ri.gilfanov@yandex.ru',
    'maintainer': 'Ruslan Ilyasovich Gilfanov',
    'maintainer_email': 'ri.gilfanov@yandex.ru',
    'url': 'https://pypi.org/project/volosti-gui-kivy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
