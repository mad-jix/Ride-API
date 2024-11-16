from rest_framework import serializers
from .models import Ride,Driver, RideRequest


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

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'user', 'latitude', 'longitude', 'is_available']

    def create(self, validated_data):
        user = validated_data.get('user')
        
        if not user.is_staff:
            raise serializers.ValidationError("Only staff users can create a driver.")
        
        return Driver.objects.create(**validated_data)


class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ['id', 'ride', 'driver', 'accepted',]





        
        
