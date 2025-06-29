from django.db import models
from apps.Measurements.models import PatMeasurement
from core.abstractModels.models import ConnectionPoint, ObservableModel


# Create your models here.

#Model used for connectors
class Connector(ObservableModel):
    name = models.TextField()
    section = models.FloatField()
    correctColor = models.BooleanField()
    startConnectionPointType = models.TextField()
    endConnectionPointType = models.TextField()
    startConnectionPoint = models.ForeignKey(ConnectionPoint, on_delete=models.CASCADE, related_name='start_connectors')
    endConnectionPoint = models.ForeignKey(ConnectionPoint, on_delete=models.SET_NULL, related_name='end_connectors', null=True)
    measurement = models.ForeignKey(PatMeasurement, on_delete=models.SET_NULL, null=True)