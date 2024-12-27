from django.db import models

# Create your models here.


class PlantImage(models.Model):
    image = models.ImageField(upload_to='plant_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uploaded_at)
