from django.urls import path
from .views import *

urlpatterns = [
    path('', ListOutletView.as_view(), name='listOutlets'),
    path('<int:sector_id>', ListFilteredBySectorOutletView.as_view(), name='listFilteredBySectorOutlets'),
    path('CircuitBreaker/', ListFilteredByEmptyCircuitBreakerOutletView.as_view(), name='listFilteredByEmptyCircuitBreakerOutletView'),
    path('new/', CreateOutletView.as_view(), name='createOutlet'),
    path('<int:pk>', UpdateOutletView.as_view(), name='updateOutlet'),
    path('CircuitBreaker/<int:pk>', UpdateOutletView.as_view(), name='updateOutletCircuitBreaker'),
]