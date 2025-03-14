from rest_framework import serializers
from .models import *

#Serializer used to @GET all circuit breakers
class ListCircuitBreakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircuitBreaker
        fields = ['id', 'name']

#Serializer used to @PATCH all circuit breakers
class UpdateCircuitBreakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircuitBreaker
        fields = ['I', 'deltaN', 'half', 'In', 'twoIn', 'fiveIn', 'degrees', 'observations', 'measurement']

#Serializer used to @POST a circuit breaker
class CreateCircuitBreakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircuitBreaker
        fields = '__all__'
