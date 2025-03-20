from django.urls import path
from .views import *

urlpatterns = [
    path('<str:startType>/<str:endType>', ListConnectorsView.as_view(), name='listConnectors'),
    path('<str:endType>', ListConnectorsByEndTypeView.as_view(), name='listEndConnectorTypeFilteredConnectors'),
    path('<str:endType>/Null/', ListConnectorsByEndTypeView.as_view(), name='listEndConnectorTypeFilteredConnectors'),
    path('<str:startType>/<str:endType>/<int:id_filter>', ListFilteredConnectorsView.as_view(), name='listFilteredConnectors'),
    path('Update/<int:pk>/', UpdateConnectorView.as_view(), name='updateConnector'),
    path('<int:pk>/', UpdateEndConnectionPointConnectorView.as_view(), name='updateEndConnectionPointConnector'),
    path('new/', CreateConnectorView.as_view(), name='createConnector'),
]