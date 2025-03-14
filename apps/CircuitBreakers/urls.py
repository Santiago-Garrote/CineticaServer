from django.urls import path
from .views import *

urlpatterns = [
    path('', ListCircuitBreakerView.as_view(), name='listCircuitBreakers'),
    path('<int:panel_id>', ListFilteredCircuitBreakerView.as_view(), name='listFilteredCircuitBreakers'),
    path('new/', CreateCircuitBreakerView.as_view(), name='createCircuitBreaker'),
    path('<int:pk>', UpdateCircuitBreakerView.as_view(), name='updateCircuitBreaker'),
]