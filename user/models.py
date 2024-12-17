from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('rider', 'Rider'),
        ('driver', 'Driver'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='rider')

    def save(self, *args, **kwargs):
        if not self.is_superuser:
            if self.role == 'driver':
                self.is_staff = True
            else:
                self.is_staff = False
        super().save(*args, **kwargs)

    def is_driver(self):
        return self.role == 'driver'

    def is_rider(self):
        return self.role == 'rider'
