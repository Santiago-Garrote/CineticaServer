from django.db import models

# Create your models here.

#Model used for Tools
class Tool(models.Model):
    name = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    calibrationDate = models.DateField()

    def save(self, *args, **kwargs):
        self.name = f'{self.brand} - {self.model} - Serie N° {self.serial}'
        super(Tool, self).save(*args, **kwargs)