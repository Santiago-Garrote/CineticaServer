from django.urls import path
from .views import *

urlpatterns = [
    path('', ListJavelinsView.as_view(), name='listJavelins'),
    path('<int:sector_id>', ListFilteredJavelinsView.as_view(), name='listFilteredJavelins'),
    path('new/', CreateJavelinView.as_view(), name='createJavelin'),
    path('<int:pk>', UpdateJavelinView.as_view(), name='updateJavelin'),
]