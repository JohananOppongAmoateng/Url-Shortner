from django.db.models import Manager

class ActiveLinkManager(Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(active=True)