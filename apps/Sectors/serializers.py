from rest_framework import serializers
from .models import *

#Serializer used to @GET all sectors
class ListSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'name']

#Serializer used to @POST a sector
class CreateSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'