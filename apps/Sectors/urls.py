from django.urls import path
from .views import *

urlpatterns = [
    path('', ListSectorsView.as_view(), name='listSectors'),
    path('new/', CreateSectorsView.as_view(), name='createSectors'),
    path('<int:business_id>', ListFilteredSectorsView.as_view(), name='listFilteredSectors'),
]