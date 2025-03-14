from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.CircuitBreakers.models import *
from apps.CircuitBreakers.serializers import *


# Create your views here.

#View used to @GET all circuit breakers
class ListCircuitBreakerView(ListAPIView):
    queryset = CircuitBreaker.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListCircuitBreakerSerializer

#View used to @GET all circuit breakers filtered by panel
class ListFilteredCircuitBreakerView(ListAPIView):
    queryset = CircuitBreaker.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListCircuitBreakerSerializer

    def get_queryset(self):
        panel_id = self.kwargs['panel_id']
        return CircuitBreaker.objects.filter(panel_id=panel_id)

#View used to @PATCH all circuit breakers
class UpdateCircuitBreakerView(UpdateAPIView):
    queryset = CircuitBreaker.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateCircuitBreakerSerializer

#View used to @GET all circuit breakers
class CreateCircuitBreakerView(CreateAPIView):
    queryset = CircuitBreaker.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCircuitBreakerSerializer
