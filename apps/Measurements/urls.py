from django.urls import path
from .views import *

urlpatterns = [
    path('', ListActiveMeasurement.as_view(), name='listActiveMeasurements'),
    path('new/', CreateMeasurement.as_view(), name='createMeasurement'),
    path('<int:pk>', UpdateMeasurement.as_view(), name='updateMeasurement'),
]