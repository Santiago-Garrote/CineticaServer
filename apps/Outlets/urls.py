from django.urls import path
from .views import *

urlpatterns = [
    path('', ListOutletView.as_view(), name='listOutlets'),
    path('<int:sector_id>', ListFilteredBySectorOutletView.as_view(), name='listFilteredBySectorOutlets'),
    path('CircuitBreaker/<str:sector_id>/Null/', ListFilteredByEmptyCircuitBreakerOutletView.as_view(), name='listFilteredByEmptyCircuitBreakerOutletView'),
    path('new/', CreateOutletView.as_view(), name='createOutlet'),
    path('Update/<int:pk>', UpdateOutletView.as_view(), name='updateOutlet'),
    path('<int:pk>/', UpdateCircuitBreakerOfOutletView.as_view(), name='updateCircuitBreakerOfOutlet'),
    path('CircuitBreaker/<int:pk>', UpdateOutletView.as_view(), name='updateOutletCircuitBreaker'),
]