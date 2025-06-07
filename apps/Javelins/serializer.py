from rest_framework import serializers
from apps.Javelins.models import Javelin


#Serializer used to @GET all javelins
class ListJavelinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Javelin
        fields = ['id', 'name']

#Serializer used to @PATCH a javelin
class UpdateJavelinSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Javelin
        fields = ['id', 'status', 'measurementValue', 'observations', 'measurement']

#Serializer used to @POST a javelin
class CreateJavelinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Javelin
        fields = '__all__'
