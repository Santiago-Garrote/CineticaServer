from rest_framework import serializers
from .models import *

#Serializer used for @POST
class CreateToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

#Serializer used for @GET
class ListToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name']