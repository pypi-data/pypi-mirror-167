import logging

import requests
from time import sleep


def check_proxy(proxy) -> bool:
    proxy_link = proxy.url
    for i in range(4):
        try:
            proxy = {
                "http": proxy_link,
                "https": proxy_link,
            }
            resp = requests.get("https://api.ipify.org?format=json", proxies=proxy)
            resp.raise_for_status()
            return True
        except Exception as err:
            logging.warning(err)
            sleep(2)
            continue
    return False
