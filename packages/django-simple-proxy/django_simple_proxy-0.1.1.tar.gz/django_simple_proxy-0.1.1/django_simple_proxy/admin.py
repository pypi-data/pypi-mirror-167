from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . import models, actions


@admin.register(models.Proxy)
class ProxyAdmin(ImportExportModelAdmin):
    list_display = ("url", "enabled", "check", "comment")
    actions = [actions.check_proxy]
