from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from apps.Measurements.models import Measurement
from .serializers import *

# Create your views here.

#View used to @GET a Measurement not ended
class ListActiveMeasurement(ListAPIView):
    queryset = Measurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListMeasurementSerializer

    def get_queryset(self):
        return Measurement.objects.filter(endDate__isnull=True)

#View used to @PATCH a Measurement
class UpdateMeasurement(UpdateAPIView):
    queryset = Measurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateMeasurementSerializer

#View used to @POST a Measurement
class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateMeasurementSerializer