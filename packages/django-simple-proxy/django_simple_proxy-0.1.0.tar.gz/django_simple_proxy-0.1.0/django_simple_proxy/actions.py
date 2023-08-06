from .tasks import check_proxy_task


def check_proxy(self, request, queryset):
    check_proxy_task.delay(queryset)


check_proxy.short_description = 'Проверить'
