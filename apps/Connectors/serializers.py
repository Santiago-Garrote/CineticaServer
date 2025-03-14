from rest_framework import serializers
from .models import *

#Serializer used to @GET all connectors
class ListConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector
        fields = ['id', 'name', 'startConnectionPointType', 'endConnectionPointType']

#Serializer used to @PATCH a connector
class UpdateConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector
        fields = ['section', 'correctColor', 'observations', 'measurement', 'endConnectionPoint']

#Serializer used to @POST a connector
class CreateConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector
        fields = ['name', 'section', 'correctColor', 'startConnectionPointType', 'endConnectionPointType', 'startConnectionPoint', 'observations', 'measurement' ]

