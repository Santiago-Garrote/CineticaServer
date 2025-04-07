from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from apps.Measurements.models import PatMeasurement
from .serializers import *

# Create your views here.

#View used to @GET a Pat Measurement not ended
class ListActivePATMeasurement(ListAPIView):
    queryset = PatMeasurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPATMeasurementSerializer

    def get_queryset(self):
        return PatMeasurement.objects.filter(endDate__isnull=True)

#View used to @PATCH a Pat Measurement
class UpdatePATMeasurement(UpdateAPIView):
    queryset = PatMeasurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePATMeasurementSerializer

#View used to @POST a Pat Measurement
class CreatePATMeasurement(CreateAPIView):
    queryset = PatMeasurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreatePATMeasurementSerializer

#View used to @GET a Dif Measurement not ended
class ListActiveDifMeasurement(ListAPIView):
    queryset = PatMeasurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListDifMeasurementSerializer

    def get_queryset(self):
        return PatMeasurement.objects.filter(endDate__isnull=True)

#View used to @PATCH a Dif Measurement
class UpdateDifMeasurement(UpdateAPIView):
    queryset = PatMeasurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateDifMeasurementSerializer

#View used to @POST a Dif Measurement
class CreateDifMeasurement(CreateAPIView):
    queryset = PatMeasurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateDifMeasurementSerializer