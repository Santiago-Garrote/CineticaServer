from django.db import models
from polymorphic.models import PolymorphicModel

from apps.Businesses.models import Business
from apps.Tools.models import Tool


# Create your abstract models here.

#This is the class which says that a model should have possible observations.
class ObservableModel(PolymorphicModel):
    observations = models.TextField(blank=True)

#This is the class which is either at the start or end of a connector
class ConnectionPoint(ObservableModel):
    name = models.TextField()

class Measurement(PolymorphicModel):
    name = models.TextField(blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField(null=True)
    methodology = models.TextField()
    observations = models.TextField(blank=True)
