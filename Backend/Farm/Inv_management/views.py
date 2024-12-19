from django.shortcuts import render
from .models import Product

def inventory_report(request):
    products = Product.objects.all()
    return render(request, 'inv.html', {'products': products})


