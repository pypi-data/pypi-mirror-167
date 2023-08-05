# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['disbase',
 'disbase.app',
 'disbase.internal',
 'disbase.internal.gateway',
 'disbase.internal.http',
 'disbase.mod']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'colorlog>=6.6.0,<7.0.0',
 'discord-typings>=0.5.0,<0.6.0']

extras_require = \
{'boost': ['uvloop>=0.16.0,<0.17.0',
           'cchardet>=2.1.7,<3.0.0',
           'aiodns>=3.0.0,<4.0.0',
           'Brotli>=1.0.9,<2.0.0']}

setup_kwargs = {
    'name': 'disbase',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'VincentRPS',
    'author_email': 'vincentbusiness55@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
