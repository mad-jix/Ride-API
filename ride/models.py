from django.db import models
from django.contrib.auth.models import User
from driver.models import Driver

class Ride(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

    rider = models.ForeignKey(User, related_name='rides_as_rider', on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='requested')
    latitude = models.FloatField(default=0.0) 
    longitude = models.FloatField(default=0.0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} - {self.rider.username} to {self.dropoff_location}"
    

class RideRequest(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="requests")
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='ride_requests')
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"RideRequest for Ride {self.ride.id} by Driver {self.driver.id if self.driver else 'N/A'}"