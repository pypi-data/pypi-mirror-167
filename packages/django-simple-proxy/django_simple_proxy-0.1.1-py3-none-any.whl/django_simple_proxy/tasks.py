from django_rq import job
from .models import Proxy
from .tools.check import check_proxy
from logging import getLogger

logger = getLogger(__name__)


@job('high', timeout=60 * 60 * 10, result_ttl=1)  # 10 hours timeout
def check_proxy_task(queryset=None):
    dead_proxy = []

    for proxy in queryset or Proxy.objects.all():
        print(f"Check {proxy.url}")
        if not check_proxy(proxy):
            logger.error(f"PROXY DEAD {proxy.url}")
            dead_proxy.append(proxy.url)
            proxy.check = False
            proxy.save(update_fields=["check"])
        else:
            proxy.check = True
            proxy.save(update_fields=["check"])

    if dead_proxy:
        raise RuntimeError(f"Some proxies are dead: {dead_proxy}")
