from django.db import models
from polymorphic.models import PolymorphicModel

# Create your abstract models here.

#This is the class which is either at the start or end of a connector
class ConnectionPoint(PolymorphicModel):
    name = models.CharField(max_length=100)
