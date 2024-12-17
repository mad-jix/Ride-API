from django.contrib.auth import authenticate

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import  DriverRegistrationSerializer,RiderRegistrationSerializer,UserLoginSerializer


class RiderRegistrationView(APIView):
    serializer_class = RiderRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=RiderRegistrationSerializer,
        responses={
            200: openapi.Response('User created  successful', examples={
                'application/json': {
                    'message': 'User created successful'
                }
            }),
            400: openapi.Response('Bad Request'),
            401: openapi.Response('Unauthorized')
        }
    )
    
    def post(self, request):
        serializer = RiderRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Rider registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DriverRegistrationView(APIView):
    serializer_class = DriverRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(
        request_body=DriverRegistrationSerializer,
        responses={
            200: openapi.Response('User created  successful', examples={
                'application/json': {
                    'message': 'User created successful'
                }
            }),
            400: openapi.Response('Bad Request'),
            401: openapi.Response('Unauthorized')
        }
    )
    def post(self, request):
        serializer = DriverRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Driver registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserLoginSerializer,
        responses={
            200: openapi.Response('Login successful', examples={
                'application/json': {
                    'refresh': 'string',
                    'access': 'string',
                    'token': 'string',
                    'message': 'Login successful'
                }
            }),
            400: openapi.Response('Bad Request'),
            401: openapi.Response('Unauthorized')
        }
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                'id': user.id,
                "role": user.role,
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
