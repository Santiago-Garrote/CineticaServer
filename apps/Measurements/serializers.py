from rest_framework import serializers
from .models import *

#Serializer used to @GET a PAT Measurement
class ListPATMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatMeasurement
        fields = ['id', 'name']

#Serializer used to @PATCH a PAT Measurement
class UpdatePATMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatMeasurement
        fields = ['endDate']

#Serializer used to @POST a PAT Measurement
class CreatePATMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatMeasurement
        fields = '__all__'

#Serializer used to @GET a Dif Measurement
class ListDifMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifMeasurement
        fields = ['id', 'name']

#Serializer used to @PATCH a Dif Measurement
class UpdateDifMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifMeasurement
        fields = ['endDate']

#Serializer used to @POST a Dif Measurement
class CreateDifMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifMeasurement
        fields = '__all__'
