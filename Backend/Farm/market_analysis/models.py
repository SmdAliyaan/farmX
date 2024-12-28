from django.db import models

class CropPrice(models.Model):
    crop_name = models.CharField(max_length=100)
    market = models.CharField(max_length=100, default='Agmarknet')
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.crop_name} - ₹{self.price} ({self.market})"
