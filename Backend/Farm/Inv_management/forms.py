
# from django import forms
# from .models import Product

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             'name', 
#             'price', 
#             'quantity_total', 
#             'date_bought', 
#             'date_expiration', 
#             'category', 
#             'quantity_remaining'
#         ]

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'quantity_total', 'date_bought',
            'date_expiration', 'category', 'quantity_remaining'
        ]
