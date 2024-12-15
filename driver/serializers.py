from rest_framework import serializers

from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'driver', 'latitude', 'longitude', 'is_available']

    def create(self, validated_data):
        driver = validated_data.get('driver')
        
        if not driver.is_staff:
            raise serializers.ValidationError("Only staff users can create a driver.")
        
        return Driver.objects.create(**validated_data)