from .models import Proxy
from .tools.check import check_proxy
from logging import getLogger

logger = getLogger(__name__)


def check_proxy_task(queryset=None):
    dead_proxy = []

    for proxy in queryset or Proxy.objects.all():
        print(f"Check {proxy.url}")
        if not check_proxy(proxy):
            logger.error(f"PROXY DEAD {proxy.url}")
            dead_proxy.append(proxy.url)
            proxy.is_checked = False
            proxy.save(update_fields=["check"])
        else:
            proxy.is_checked = True
            proxy.save(update_fields=["check"])

    if dead_proxy:
        raise RuntimeError(f"Some proxies are dead: {dead_proxy}")
