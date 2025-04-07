from django.db import models
from polymorphic.models import PolymorphicModel

from apps.Businesses.models import Business
from apps.Tools.models import Tool


# Create your abstract models here.

#This is the class which is either at the start or end of a connector
class ConnectionPoint(PolymorphicModel):
    name = models.CharField(max_length=500)

class Measurement(PolymorphicModel):
    name = models.CharField(max_length=300, blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField(null=True)
    methodology = models.CharField(max_length=300)
    observations = models.TextField(blank=True)
