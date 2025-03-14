from rest_framework import serializers
from .models import *

#Serializer used to @GET a Measurement
class ListMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'name']

#Serializer used to @PATCH a Measurement
class UpdateMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['endDate']

#Serializer used to @POST a Measurement
class CreateMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'