from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.Outlets.models import Outlet
from apps.Outlets.serializers import *


# Create your views here.

#View used to @GET all outlets
class ListOutletView(ListAPIView):
    queryset = Outlet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListOutletSerializer

#View used to @GET all outlets
class ListFilteredBySectorOutletView(ListAPIView):
    queryset = Outlet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListOutletSerializer

    def get_queryset(self):
        sector_id = self.kwargs['sector_id']
        return Outlet.objects.filter(sector_id=sector_id)

#View used to @GET all outlets
class ListFilteredByEmptyCircuitBreakerOutletView(ListAPIView):
    queryset = Outlet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListOutletSerializer

    def get_queryset(self):
        return Outlet.objects.filter(
            circuitBreaker__isnull=True,
            sector__business_id=self.kwargs['sector_id']
        )

#View used to @PATCH an outlet
class UpdateOutletView(UpdateAPIView):
    queryset = Outlet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateOutletSerializer

#View used to @PATCH an outlet
class UpdateCircuitBreakerOfOutletView(UpdateAPIView):
    queryset = Outlet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateOutletCircuitBreakerSerializer

#View used to @PATCH the circuit breaker of an outlet
class UpdateOutletCircuitBreakerView(UpdateAPIView):
    queryset = Outlet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateOutletCircuitBreakerSerializer

#View used to @POST an outlet
class CreateOutletView(CreateAPIView):
    queryset = Outlet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateOutletSerializer