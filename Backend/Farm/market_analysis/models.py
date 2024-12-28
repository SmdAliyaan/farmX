from django.db import models

class CropPrice(models.Model):
    crop_name = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.crop_name} in {self.market} - ₹{self.price} on {self.date}"

