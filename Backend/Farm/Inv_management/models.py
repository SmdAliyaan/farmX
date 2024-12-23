# from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     quantity = models.PositiveIntegerField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


#     def __str__(self):
#         return self.name

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)  # Added image field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_total = models.IntegerField()
    date_bought = models.DateField(null=True, blank=True)  # Make field nullable
    date_expiration = models.DateField(null=True, blank=True)  # Make field nullable
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_remaining = models.IntegerField()

    def __str__(self):
        return self.name