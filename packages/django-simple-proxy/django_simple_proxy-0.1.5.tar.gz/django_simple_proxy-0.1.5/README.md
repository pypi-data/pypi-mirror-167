# django_simple_proxy
Simple Proxy for Python Django framework

# Installation
```
pip install django-simple-proxy
```

Then add `django_simple_proxy` to `INSTALLED_APPS`

# Usage
First, set Proxy in the database using the admin panel.

Manually, with `requests` library.
```
import requests

from django_simple_proxy.tools import random_proxy

proxy_url = random_proxy()
proxies = {'http': proxy_url, 'https': proxy_url}
response = requests.get(url, proxies=proxies)
```

Or using `get_request` / `post_request`:
```
from django_simple_proxy.tools import get_request

response = get_request(url)
```
