from django.db import models
from .queryset import ProxyQueryset


# Create your models here.
class Proxy(models.Model):
    url = models.CharField(verbose_name="Ссылка на прокси-сервер", max_length=200)
    enabled = models.BooleanField(verbose_name="Включён", default=True, blank=True)
    comment = models.TextField(verbose_name="Комментарий", blank=True, default="")
    check = models.BooleanField(verbose_name="Проверена", default=True, blank=True)

    objects = ProxyQueryset.as_manager()

    class Meta:
        verbose_name = "Прокси"
        verbose_name_plural = "Прокси"
        ordering = ['url']
