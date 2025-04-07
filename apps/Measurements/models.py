from django.db import models
from apps.Businesses.models import Business
from apps.Tools.models import Tool
from core.abstractModels.models import Measurement


# Create your models here.

#Model used for Measurements
class PatMeasurement(Measurement):
    def save(self, *args, **kwargs):
        difMeasurement = models.ForeignKey('DifMeasurement', on_delete=models.SET_NULL, null=True)

        self.name = f'Medicion P.A.T. - {self.business.name} - {self.startDate.date()}'
        super(Measurement, self).save(*args, **kwargs)

class DifMeasurement(Measurement):
    def save(self, *args, **kwargs):
        self.name = f'Medicion Dif. - {self.business.name} - {self.startDate.date()}'
        super(Measurement, self).save(*args, **kwargs)
