from django.db import transaction

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from .models import Driver
from .serializers import DriverSerializer,UpdateDriverSerializer
from .permissions import IsDriver
 
from ride.serializers import RideRequestSerializer
from ride.models import RideRequest


class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsDriver]

    def perform_create(self, serializer):
        serializer.save()


class DriverListView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]  


class RideRequestAcceptView(generics.UpdateAPIView):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        ride_request = self.get_object()

        try:
            driver = request.user.driver
        except Driver.DoesNotExist:
            raise ValidationError("You are not authorized to accept this ride request.")

        if not ride_request.driver or driver.id != ride_request.driver.id:
            raise ValidationError("You are not the assigned driver for this ride request.")


        if ride_request.accepted:
            raise ValidationError("This ride request has already been accepted.")

        with transaction.atomic():
            ride_request.accepted = True
            ride_request.save()

            ride = ride_request.ride
            ride.status = 'started'
            ride.save()

            driver.is_available = False
            driver.save()

        return Response({
            "message": "Ride request accepted successfully.",
            "ride_request": RideRequestSerializer(ride_request).data
        }, status=status.HTTP_200_OK)
    

class UpdateDriverView(generics.UpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = UpdateDriverSerializer
    permission_classes = [IsDriver]

    def patch(self, request, *args, **kwargs):
        try:
            driver = self.get_object()
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(driver, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)