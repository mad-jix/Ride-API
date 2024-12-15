from rest_framework import serializers
from .models import Ride,RideRequest


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'rider', 'pickup_location', 'dropoff_location', 'status', 'latitude', 'longitude', 'created_at', 'updated_at']

    def create(self, validated_data):
    
        ride = Ride.objects.create(
            rider=validated_data['rider'],
            pickup_location=validated_data['pickup_location'],
            dropoff_location=validated_data['dropoff_location'],
            status='booked',  
            latitude=validated_data.get('latitude', 0.0),
            longitude=validated_data.get('longitude', 0.0),
        )
        return ride




class RideStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['status']




class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ['id', 'ride', 'driver', 'accepted',]





        
        
