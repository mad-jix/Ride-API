from django.urls import path
from .views import RideCreateView, RideDetail, ListRides,UpdateRideStatusView,RideRequestCreateView,RideRequestAcceptView,ListRidesRequest
urlpatterns = [
    path('ridecreate/', RideCreateView.as_view(), name='ride-create'),
    path('rides/<int:pk>/', RideDetail.as_view(), name='ride_detail'),
    path('rides/all/', ListRides.as_view(), name='list_rides'),
    path('api/rides/<int:pk>/status/', UpdateRideStatusView.as_view(), name='update_ride_status'),
    path('ride-request/create/', RideRequestCreateView.as_view(), name='ride-request-create'),
    path('ride-request/<int:pk>/accept/', RideRequestAcceptView.as_view(), name='accept the rice'),
    path('allrequest/', ListRidesRequest.as_view(), name='list_rides-request'),
    
]