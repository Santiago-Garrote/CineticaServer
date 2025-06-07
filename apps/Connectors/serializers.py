from rest_framework import serializers
from .models import *

#Serializer used to @GET all connectors
class ListConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector
        fields = ['id', 'name', 'startConnectionPointType', 'endConnectionPointType']

#Serializer used to @GET all connectors
class ListConnectorNullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector
        fields = ['id', 'name', 'startConnectionPointType', 'endConnectionPointType', 'endConnectionPoint']

#Serializer used to @PATCH a connector
class UpdateConnectorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Connector
        fields = ['id', 'section', 'correctColor', 'observations', 'measurement']

#Serializer used to @PATCH a connector
class UpdateEndConnectionPointConnectorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Connector
        fields = ['id', 'endConnectionPoint']


#Serializer used to @POST a connector
class CreateConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector
        fields = '__all__'