from django.urls import path
from .views import *

urlpatterns = [
    # ObservationImage URLs
    path('observationimage/', ListObservationImagesView.as_view(), name='listObservationImages'),
    path('observationimage/<int:observation_id>/', ListFilteredObservationImagesView.as_view(), name='listFilteredObservationImages'),
    path('observationimage/new/', CreateObservationImageView.as_view(), name='createObservationImage'),
]
