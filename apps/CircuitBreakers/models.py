from django.db import models

from apps.Measurements.models import Measurement
from apps.Panels.models import Panel


# Create your models here.

#Model used for a circuit breaker
class CircuitBreaker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    I = models.SmallIntegerField()
    deltaN = models.SmallIntegerField()
    half = models.SmallIntegerField()
    In = models.FloatField()
    twoIn = models.FloatField()
    fiveIn = models.FloatField()
    degrees = models.FloatField()
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    observations = models.TextField(blank=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True)



