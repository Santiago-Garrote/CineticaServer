from django.urls import path
from .views import *

urlpatterns = [
    path('', ListMeasurement.as_view(), name='listMeasurements'),
    path('new/', CreateMeasurement.as_view(), name='createMeasurement'),
    path('<int:pk>', UpdateMeasurement.as_view(), name='updateMeasurement'),
]