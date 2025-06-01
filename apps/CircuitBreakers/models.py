from django.db import models

from apps.Measurements.models import DifMeasurement
from apps.Panels.models import Panel
from apps.Sectors.models import Sector
from core.abstractModels.models import ObservableModel


# Create your models here.

#Model used for a circuit breaker
class CircuitBreaker(ObservableModel):
    name = models.TextField()
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    brand = models.TextField()
    model = models.TextField()
    I = models.SmallIntegerField()
    deltaN = models.SmallIntegerField()
    half = models.SmallIntegerField()
    In = models.FloatField()
    twoIn = models.FloatField()
    fiveIn = models.FloatField()
    degrees = models.FloatField()
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    measurement = models.ForeignKey(DifMeasurement, on_delete=models.SET_NULL, null=True)



