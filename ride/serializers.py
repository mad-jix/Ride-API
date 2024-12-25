from rest_framework import serializers
from .models import Ride,RideRequest


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'rider', 'pickup_location', 'dropoff_location', 'status', 'latitude', 'longitude', 'created_at', 'updated_at']
        read_only_fields = ['rider', 'status', 'created_at', 'updated_at']  

    def create(self, validated_data):
        request = self.context.get('request')  
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("A logged-in user is required to create a ride.")
        
        validated_data['rider'] = request.user  
        validated_data['status'] = 'booked'  
        
        return super().create(validated_data)  




class RideStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['status']




class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ['id', 'ride', 'driver', 'accepted',]





        
        
