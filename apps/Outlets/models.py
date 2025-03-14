from django.db import models

from apps.CircuitBreakers.models import CircuitBreaker
from apps.Measurements.models import Measurement
from apps.Sectors.models import Sector
from core.abstractModels.models import ConnectionPoint

# Create your models here.

class Outlet(ConnectionPoint):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    circuitBreaker = models.ForeignKey(CircuitBreaker, on_delete=models.SET_NULL, null=True)
    usoPat = models.CharField(max_length=50)
    observations = models.TextField(blank=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True)