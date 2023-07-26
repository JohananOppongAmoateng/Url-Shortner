from django.db import models
from .managers import ActiveLinkManager
# Create your models here.
from .utils import generate_random_id
class Link(models.Model):
    target_url = models.URLField(max_length=250)
    description = models.CharField(max_length=255)
    created_date = models.DateField(auto_now=True)
    shorten_url = models.CharField(default=generate_random_id())
    active = models.BooleanField(default=True)
    objects = models.Manager()
