from rest_framework import serializers

from apps.Outlets.models import Outlet


#View used to @GET all outlets
class ListOutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ['id', 'name']

#View used to @PATCH an outlet
class UpdateOutletSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Outlet
        fields = ['id','observations', 'measurement']

#View used to @PATCH the circuit breaker of an outlet
class UpdateOutletCircuitBreakerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Outlet
        fields = ['id','circuitBreaker']


#View used to @POST an outlet
class CreateOutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = '__all__'