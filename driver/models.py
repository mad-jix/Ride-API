from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='driver', on_delete=models.SET_NULL, null=True, blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)