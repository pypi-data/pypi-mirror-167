# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_simple_proxy',
 'django_simple_proxy.migrations',
 'django_simple_proxy.tools']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'django-simple-proxy',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alex Polev',
    'author_email': 'apolevki09@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
