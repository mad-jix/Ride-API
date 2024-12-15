from django.urls import path
from .views import UserSignupView, UserLoginView,DriverSignupView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('driversignup/', DriverSignupView.as_view(), name='driversignup'),
    path('login/', UserLoginView.as_view(), name='login'),
]