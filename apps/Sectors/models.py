from django.db import models
from apps.Businesses.models import Business
# Create your models here.

#Model used for Sectors
class Sector(models.Model):
    #Data
    name = models.CharField(max_length=100)
    scheme = models.CharField(max_length=100)
    #Foreign Key to the Business where it is contained
    business = models.ForeignKey(Business, on_delete=models.CASCADE)