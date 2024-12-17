from django.urls import path
from .views import RideCreateView, RideDetail, ListRides,UpdateRideStatusView,RideRequestCreateView,ListRidesRequest
urlpatterns = [
    path('ride-create/', RideCreateView.as_view(), name='ride-create'),
    path('detial-view/<int:pk>/', RideDetail.as_view(), name='ride_detail'),
    path('all-rides/', ListRides.as_view(), name='list_rides'),
    path('status-update/<int:pk>/', UpdateRideStatusView.as_view(), name='update_ride_status'),
    path('ride-request-create/', RideRequestCreateView.as_view(), name='ride-request-create'),
    path('all-request/', ListRidesRequest.as_view(), name='list_rides-request'),
    
]