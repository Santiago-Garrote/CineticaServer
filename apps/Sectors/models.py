from django.db import models
from apps.Businesses.models import Business
# Create your models here.

#Model used for Sectors
class Sector(models.Model):
    #Data
    name = models.TextField()
    scheme = models.TextField()
    #Foreign Key to the Business where it is contained
    business = models.ForeignKey(Business, on_delete=models.CASCADE)