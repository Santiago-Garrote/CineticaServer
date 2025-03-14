from rest_framework import serializers
from .models import Business

class GetBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id','name']

class PostBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'