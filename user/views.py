from django.contrib.auth import authenticate


from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from .serializers import SignupSerializer,LoginSerializer,DriverSignupSerializer

# Create your views here.
class UserSignupView(APIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema(
        request_body=SignupSerializer,
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
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DriverSignupView(APIView):
    serializer_class = DriverSignupSerializer
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema(
        request_body=DriverSignupSerializer,
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
        serializer = DriverSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

class UserLoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=LoginSerializer,
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
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'is_staff': user.is_staff,
                    'id': user.id,  # Added comma here
                    'message': 'Login successful'
                }, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)