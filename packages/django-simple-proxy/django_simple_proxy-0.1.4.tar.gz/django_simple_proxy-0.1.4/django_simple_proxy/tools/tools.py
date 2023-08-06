from typing import Optional
import requests
import time
from logging import getLogger
import warnings
from urllib3.exceptions import InsecureRequestWarning
from django.conf import settings

from ..models import Proxy
from .useragent import random_user_agent
from requests.adapters import HTTPAdapter, Retry


logger = getLogger(__name__)


def random_proxy() -> Optional[str]:
    obj = Proxy.objects.random()
    return obj.url if obj else None


def _abstract_request_proxy(url: str, method, **kwargs):
    proxies = Proxy.objects.all().values_list('url', flat=True)

    retries = getattr(settings, 'PROXY_RETRIES', 3)
    for retry in range(retries):
        if len(proxies) == 0:
            break

        for proxy_link in proxies:
            proxy = {
                "http": proxy_link,
                "https": proxy_link,
            }

            try:
                logger.debug(f"Use {proxy_link} for {url}...")
                resp = _abstract_direct(url, method=method, proxies=proxy, **kwargs)
                if resp.status_code not in (200, 404):  # для этих статусов не нужно пытаться сделать запрос второй раз
                    resp.raise_for_status()
                return resp
            except Exception as err:
                logger.warning(err)
                logger.warning("Retry with another proxy and user-agent...")
                continue

        time.sleep(5)

    # Now try without proxy
    return _abstract_direct(url, method=method, **kwargs)


def _abstract_direct(url: str, method, **kwargs):
    headers = {
        'User-Agent': random_user_agent(),
    }
    if "headers" in kwargs:
        headers.update(kwargs.pop("headers"))
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=InsecureRequestWarning)
        return method(url, headers=headers, timeout=60, verify=False, **kwargs)


def get_request(url, **kwargs):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=Retry(total=5, status_forcelist=[500, 502, 503, 504])))
    s.mount('https://', HTTPAdapter(max_retries=Retry(total=5, status_forcelist=[500, 502, 503, 504])))
    s.keep_alive = False
    return _abstract_request_proxy(url, s.get, **kwargs)


def post_request(url, **kwargs):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=Retry(total=5, status_forcelist=[500, 502, 503, 504, 403])))
    s.mount('https://', HTTPAdapter(max_retries=Retry(total=5, status_forcelist=[500, 502, 503, 504, 403])))
    s.keep_alive = False
    return _abstract_request_proxy(url, s.post, **kwargs)

