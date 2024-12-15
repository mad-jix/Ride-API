from django.urls import path
from .views import DriverCreateView,DriverListView,DriverUpdateView,RideRequestAcceptView

urlpatterns = [

    path('drivers/create/', DriverCreateView.as_view(), name='driver-create'),
    path('list/', DriverListView.as_view(), name='all-driverse'),
    path('drivers/<int:pk>/', DriverUpdateView.as_view(), name='driver-update'),
    path('ride/<int:pk>/accept/', RideRequestAcceptView.as_view(), name='accept-ride-request'),


]