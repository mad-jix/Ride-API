from django.urls import path
from .views import DriverCreateView,DriverListView,DriverUpdateView,RideRequestAcceptView

urlpatterns = [

    path('create', DriverCreateView.as_view(), name='driver-create'),
    path('list/', DriverListView.as_view(), name='all-driverse'),
    path('change/<int:pk>/', DriverUpdateView.as_view(), name='driver-update'),
    path('ride-accept/<int:pk>/', RideRequestAcceptView.as_view(), name='accept-ride-request'),


]