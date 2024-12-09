
from math import radians, cos, sin, sqrt, atan2

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import PermissionDenied

from driver.models import Driver
from .models import Ride, RideRequest
from .serializers import RideSerializer, DriverSerializer, RideRequestSerializer, RideStatusUpdateSerializer

class RideCreateView(generics.CreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def perform_create(self, serializer):
        serializer.save(rider=self.request.user)


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "Ride created successfully", "ride": response.data}, status=status.HTTP_201_CREATED)


class RideDetail(generics.RetrieveAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListRides(generics.ListAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateRideStatusView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideStatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_staff:
            raise PermissionDenied("Only staff users can create a driver.")
        serializer.save(user=user)



class RideRequestCreateView(generics.CreateAPIView):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer

    def get_nearby_driver(self, pickup_lat, pickup_long, threshold_distance=5):
        """
        Finds and returns the first available driver within the threshold distance.
        """
        available_drivers = Driver.objects.filter(is_available=True)
        
        def calculate_distance(lat1, long1, lat2, long2):
            # Convert latitude and longitude from degrees to radians
            lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
            dlat = lat2 - lat1
            dlong = long2 - long1
            # Haversine formula
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            radius = 6371  # Radius of Earth in kilometers
            return radius * c

        for driver in available_drivers:
            driver_distance = calculate_distance(pickup_lat, pickup_long, driver.latitude, driver.longitude)
            if driver_distance <= threshold_distance:
                return driver
        return None

    def perform_create(self, serializer):
    # Retrieve the Ride object (assuming 'ride' is part of the incoming data)
        try:
            ride_id = self.request.data.get('ride')  # Assuming 'ride' contains the ID of the Ride object
            ride = Ride.objects.get(id=ride_id)
        except (Ride.DoesNotExist, TypeError, ValueError):
            raise ValidationError('A valid Ride ID is required.')

        # Get pickup latitude and longitude from the Ride object
        pickup_lat = ride.latitude
        pickup_long = ride.longitude

        # Find an available nearby driver
        nearby_driver = self.get_nearby_driver(pickup_lat, pickup_long)

        if not nearby_driver:
            raise ValidationError('No nearby available drivers found within the specified range.')
        
        ride.status = 'requested'
        ride.save() 

        serializer.save(driver=nearby_driver, accepted=False, ride=ride)




class RideRequestAcceptView(generics.UpdateAPIView):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """
        Allows a driver to accept a ride request.
        """
        ride_request = self.get_object()

        # Ensure the requesting user is a driver and matches the assigned driver
        if not hasattr(request.user, 'driver') or request.user.driver.id != ride_request.driver.id:
            raise ValidationError("You are not authorized to accept this ride request.")

        # Check if the ride request is already accepted
        if ride_request.accepted:
            raise ValidationError("This ride request has already been accepted.")

        # Update the ride request status
        ride_request.accepted = True
        ride_request.ride.status = 'started'
        ride_request.ride.save()
        ride_request.save()

        return Response({
            "message": "Ride request accepted successfully.",
            "ride_request": RideRequestSerializer(ride_request).data
        }, status=status.HTTP_200_OK)
