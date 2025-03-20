from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import *

# Create your views here.

#View used to @GET all connectors filtered by start and end connector type
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

#View used to @GET all connectors filtered by end connector type
class ListConnectorsByEndTypeView(ListAPIView):
    queryset = Connector.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListConnectorSerializer

    def get_queryset(self):
        endType = self.kwargs['endType']
        return Connector.objects.filter(
            endConnectionPointType=endType
        )

#View used to @GET all connectors filtered by end connector type
class ListConnectorsByEndTypeView(ListAPIView):
    queryset = Connector.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListConnectorSerializer

    def get_queryset(self):
        endType = self.kwargs['endType']
        return Connector.objects.filter(
            endConnectionPointType=endType,
            endConnectionPoint__isnull=True
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

#View used to @PATCH the end connection point of a connector
class UpdateEndConnectionPointConnectorView(UpdateAPIView):
    queryset = Connector.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateEndConnectionPointConnectorSerializer

#View used to @POST a connector
class CreateConnectorView(CreateAPIView):
    queryset = Connector.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateConnectorSerializer