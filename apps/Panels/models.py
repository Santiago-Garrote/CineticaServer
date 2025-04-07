from django.db import models

from apps.Businesses.models import Business
from apps.Measurements.models import PatMeasurement
from core.abstractModels.models import ConnectionPoint


# Create your models here.

#This is the model used for panels
class Panel(ConnectionPoint):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    hasBar = models.BooleanField()
    section = models.FloatField()
    observation = models.TextField(blank=True)
    measurement = models.ForeignKey(PatMeasurement, on_delete=models.SET_NULL, null=True)

#This is the model used for sectional panels
class SectionalPanel(Panel):
    pass

#This is the model used for principal panels
class PrincipalPanel(Panel):
    hasProtectors = models.BooleanField()