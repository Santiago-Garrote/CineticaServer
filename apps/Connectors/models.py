from django.db import models
from apps.Measurements.models import PatMeasurement
from core.abstractModels.models import ConnectionPoint

# Create your models here.

#Model used for connectors
class Connector(models.Model):
    name = models.CharField(max_length=100)
    section = models.FloatField()
    correctColor = models.BooleanField()
    startConnectionPointType = models.CharField(max_length=100)
    endConnectionPointType = models.CharField(max_length=100)
    startConnectionPoint = models.ForeignKey(ConnectionPoint, on_delete=models.CASCADE, related_name='start_connectors')
    endConnectionPoint = models.ForeignKey(ConnectionPoint, on_delete=models.SET_NULL, related_name='end_connectors', null=True)
    observations = models.TextField(blank=True)
    measurement = models.ForeignKey(PatMeasurement, on_delete=models.SET_NULL, null=True)