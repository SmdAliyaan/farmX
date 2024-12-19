# views.py

# from django.shortcuts import render, redirect
# from .forms import ProductForm
# from .models import Product

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('inventory_report')  # Redirect to inventory report after adding product
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form': form})

# def inventory_report(request):
#     products = Product.objects.all()
#     return render(request, 'inv.html', {'products': products})
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_report')  # Redirect to inventory report after adding product
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def inventory_report(request):
    products = Product.objects.all()
    return render(request, 'inv.html', {'products': products})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('inventory_report')
    return render(request, 'confirm_delete.html', {'product': product})
