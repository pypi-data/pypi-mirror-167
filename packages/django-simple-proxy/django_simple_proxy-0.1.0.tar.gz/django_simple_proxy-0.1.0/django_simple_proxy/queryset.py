from django.db.models import QuerySet


class ProxyQueryset(QuerySet):
    def random(self):
        return self.filter(enabled=True).order_by('?').first()
