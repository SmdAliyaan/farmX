from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_total = models.IntegerField()
    quantity_remaining = models.IntegerField()
    date_bought = models.DateField()
    date_expiration = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

