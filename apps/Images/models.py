from django.db import models
from core.abstractModels.models import ObservableModel

#Model used for the image load for an observation
class ObservationImage(models.Model):
    content_object = models.ForeignKey(ObservableModel, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="observation_images/")
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.content_object.__class__.__name__} #{self.content_object.id}"