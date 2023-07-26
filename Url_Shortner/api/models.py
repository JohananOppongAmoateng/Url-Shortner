from django.db import models
from .managers import ActiveLinkManager
# Create your models here.

class Link(models.Model):
    target_url = models.URLField(max_length=250)
    description = models.CharField(max_length=255)
    created_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()