from django.db import models

# Create your models here.

#Model used for Tools
class Tool(models.Model):
    name = models.TextField(blank=True)
    brand = models.TextField()
    model = models.TextField()
    serial = models.TextField()
    calibrationDate = models.DateField()

    def save(self, *args, **kwargs):
        self.name = f'{self.brand} - {self.model} - Serie N° {self.serial}'
        super(Tool, self).save(*args, **kwargs)