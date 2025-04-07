from django.urls import path
from .views import *

urlpatterns = [
    path('PAT/', ListActivePATMeasurement.as_view(), name='listActivePatMeasurements'),
    path('PAT/new/', CreatePATMeasurement.as_view(), name='createPatMeasurement'),
    path('PAT/<int:pk>', UpdatePATMeasurement.as_view(), name='updatePatMeasurement'),
    path('Dif/', ListActiveDifMeasurement.as_view(), name='listActiveDifMeasurements'),
    path('Dif/new/', CreateDifMeasurement.as_view(), name='createDifMeasurement'),
    path('Dif/<int:pk>', UpdateDifMeasurement.as_view(), name='updateDifMeasurement'),
]