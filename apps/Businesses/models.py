from django.db import models

# Create your models here.

#Model used for posting a Business
class Business(models.Model):
    #Primary key
    id = models.BigIntegerField(primary_key=True)
    # Data
    CUIT = models.BigIntegerField()
    cp = models.IntegerField()
    name = models.TextField()
    province = models.TextField()
    locality = models.TextField()
    direction = models.TextField()
    soil = models.TextField()

    def save(self, *args, **kwargs):
        self.id = int(f"{self.CUIT}{self.cp}")
        super().save(*args, **kwargs)