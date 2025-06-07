from django.urls import path
from .views import *

urlpatterns = [
    # ObservationImage URLs
    path('', ListObservationImagesView.as_view(), name='listObservationImages'),
    path('<int:observation_id>/', ListFilteredObservationImagesView.as_view(), name='listFilteredObservationImages'),
    path('new/', CreateObservationImageView.as_view(), name='createObservationImage'),
]
