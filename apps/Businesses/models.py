from django.db import models

# Create your models here.

#Model used for posting a Business
class Business(models.Model):
    #Primary key
    id = models.BigIntegerField(primary_key=True)
    # Data
    CUIT = models.BigIntegerField()
    cp = models.IntegerField()
    name = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    soil = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.id = int(f"{self.CUIT}{self.cp}")