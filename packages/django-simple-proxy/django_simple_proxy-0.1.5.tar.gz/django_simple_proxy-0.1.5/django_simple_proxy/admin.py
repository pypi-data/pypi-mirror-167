from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . import models


@admin.register(models.Proxy)
class ProxyAdmin(ImportExportModelAdmin):
    list_display = ("url", "enabled", "is_checked", "comment")
