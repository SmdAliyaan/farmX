from django.db import models

class CropPrice(models.Model):
    crop_name = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)

class UserPhone(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
