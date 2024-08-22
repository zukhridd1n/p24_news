from django.db.models import Manager
from django.utils import timezone
from apps.article.choices import Status


class PublishManager(Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(status=Status.PUBLISHED)
        return queryset


class ActiveAdvertiseManager(Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(expire_date__gte=timezone.now(), is_active=True)
        return queryset