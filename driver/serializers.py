from rest_framework import serializers

from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'user', 'latitude', 'longitude', 'is_available']

    def create(self, validated_data):
        user = validated_data.get('user')
        
        if not user.is_staff:
            raise serializers.ValidationError("Only staff users can create a driver.")
        
        return Driver.objects.create(**validated_data)