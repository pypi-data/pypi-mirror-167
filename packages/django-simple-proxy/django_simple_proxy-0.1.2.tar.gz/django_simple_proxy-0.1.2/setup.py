# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_simple_proxy',
 'django_simple_proxy.migrations',
 'django_simple_proxy.tools']

package_data = \
{'': ['*']}

install_requires = \
['Django', 'django-import-export', 'requests']

setup_kwargs = {
    'name': 'django-simple-proxy',
    'version': '0.1.2',
    'description': '',
    'long_description': "# django_simple_proxy\nSimple Proxy for Python Django framework\n\n# Installation\n```\npip install django-simple-proxy\n```\n\nThen add `django_simple_proxy` to `INSTALLED_APPS`\n\n# Usage\nFirst, set Proxy in the database using the admin panel.\n\nManually, with `requests` library.\n```\nimport requests\n\nfrom django_simple_proxy.tools import random_proxy\n\nproxy_url = random_proxy()\nproxies = {'http': proxy_url, 'https': proxy_url}\nresponse = requests.get(url, proxies=proxies)\n```\n\nOr using `get_request` / `post_request`:\n```\nfrom django_simple_proxy.tools import get_request\n\nresponse = get_request(url)\n```\n",
    'author': 'Alex Polev',
    'author_email': 'apolevki09@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/volunteer-prb/django_simple_proxy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
