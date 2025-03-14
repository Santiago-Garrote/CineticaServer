from django.db import models
from apps.Businesses.models import Business
from apps.Tools.models import Tool

# Create your models here.

#Model used for Measurements
class Measurement(models.Model):
    name = models.CharField(max_length=100, blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    methodology = models.CharField(max_length=100)
    observations = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.name = f'{self.business.name} - {self.startDate.date()}'
        super(Measurement, self).save(*args, **kwargs)