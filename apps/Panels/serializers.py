from rest_framework import serializers
from apps.Panels.models import *


#Serializer used to @GET all panels
class ListPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = ['id', 'name']

#Serializer used to @GET all sectional panels
class ListSectionalPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionalPanel
        fields = ['id', 'name']

#Serializer used to @PATCH a sectional panel
class UpdateSectionalPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionalPanel
        fields = ['hasBar', 'section', 'observation', 'measurement']

#Serializer used to @POST a sectional panel
class CreateSectionalPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionalPanel
        fields = '__all__'

#Serializer used to @GET all principal panels
class ListPrincipalPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalPanel
        fields = ['id', 'name']

# Serializer used to @PATCH a principal panel
class UpdatePrincipalPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalPanel
        fields = ['hasBar', 'hasProtectors', 'section', 'observation', 'measurement']

#Serializer used to @POST a principal panel
class CreatePrincipalPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalPanel
        fields = '__all__'