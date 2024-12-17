from django.urls import path
from .views import DriverRegistrationView, RiderRegistrationView, LoginView

urlpatterns = [
    path('register-driver/', DriverRegistrationView.as_view(), name='register_driver'),
    path('register-rider/', RiderRegistrationView.as_view(), name='register_rider'),
    path('login/', LoginView.as_view(), name='login'),
]
