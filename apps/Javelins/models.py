from django.db import models

from apps.Businesses.models import Business
from apps.Measurements.models import PatMeasurement
from apps.Sectors.models import Sector
from core.abstractModels.models import ConnectionPoint

# Create your models here.

#Model used for javelins
class Javelin(ConnectionPoint):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    measurementValue = models.FloatField()
    connection = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    usoPat = models.CharField(max_length=50)
    observations = models.TextField(blank=True)
    measurement = models.ForeignKey(PatMeasurement, on_delete=models.SET_NULL, null=True)
