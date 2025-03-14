from django.urls import path
from .views import *

urlpatterns = [
    path('<str:startType>/<str:endType>', ListConnectorsView.as_view(), name='listConnectors'),
    path('<str:startType>/<str:endType>/<int:id_filter>', ListFilteredConnectorsView.as_view(), name='listFilteredConnectors'),
    path('<int:pk>', UpdateConnectorView.as_view(), name='updateConnector'),
    path('new/', CreateConnectorView.as_view(), name='createConnector'),
]