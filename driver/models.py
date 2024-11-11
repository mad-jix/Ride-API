from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.ForeignKey(User, related_name='rides_as_driver', on_delete=models.SET_NULL, null=True, blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)