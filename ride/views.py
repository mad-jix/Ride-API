import math

from django.db.models import Q

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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