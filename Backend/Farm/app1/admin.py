from django.contrib import admin

# Register your models here.

from .models import CropPrice, PricePrediction

admin.site.register(CropPrice)
admin.site.register(PricePrediction)