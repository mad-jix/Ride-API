from django.urls import path
from .views import DriverCreateView,DriverListView,UpdateDriverView,RideRequestAcceptView

urlpatterns = [

    path('create', DriverCreateView.as_view(), name='driver-create'),
    path('list/', DriverListView.as_view(), name='all-driverse'),
    path('update/<int:pk>/', UpdateDriverView.as_view(), name='driver-update'),
    path('ride-accept/<int:pk>/', RideRequestAcceptView.as_view(), name='accept-ride-request'),



]


