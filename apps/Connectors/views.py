from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.Connectors.models import Connector
from apps.Connectors.serializers import ListConnectorSerializer, UpdateConnectorSerializer, CreateConnectorSerializer


# Create your views here.

#View used to @GET all connectors
class ListConnectorsView(ListAPIView):
    queryset = Connector.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListConnectorSerializer

    def get_queryset(self):
        startType = self.kwargs['startType']
        endType = self.kwargs['endType']
        return Connector.objects.filter(
            startConnectionPointType=startType,
            endConnectionPointType=endType
        )

#View used to @GET all connectors filtered by an id
class ListFilteredConnectorsView(ListAPIView):
    queryset = Connector.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListConnectorSerializer

    def get_queryset(self):
        id_filter = self.kwargs['id_filter']
        startType = self.kwargs['startType']
        endType = self.kwargs['endType']
        return Connector.objects.filter(
            startConnectionPointType=startType,
            endConnectionPointType=endType,
            startConnectionPoint_id=id_filter,
        )

#View used to @PATCH a connector
class UpdateConnectorView(UpdateAPIView):
    queryset = Connector.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateConnectorSerializer

#View used to @POST a connector
class CreateConnectorView(CreateAPIView):
    queryset = Connector.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateConnectorSerializer