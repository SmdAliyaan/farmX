from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.phone_number})"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity_total = models.IntegerField(default=0)
    date_bought = models.DateField(null=True, blank=True)
    date_expiration = models.DateField(null=True, blank=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    quantity_remaining = models.IntegerField(default=0)

    def __str__(self):
        return self.name

