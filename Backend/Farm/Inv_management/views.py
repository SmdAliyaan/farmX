from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .forms import ProductForm
from django.contrib import messages

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventory_report')  # Redirect to inventory report after adding product
    else:
        form = ProductForm()
    
    categories = Category.objects.all()
    return render(request, 'add_inv.html', {'form': form, 'categories': categories})

def inventory_report(request):
    products = Product.objects.all()
    return render(request, 'inv.html', {'products': products})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('inventory_report')
    return render(request, 'confirm_delete.html', {'product': product})
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Retrieve the product by its primary key
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Pass the existing product to the form
        if form.is_valid():
            form.save()  # Save the updated product
            return redirect('inventory_report')  # Redirect back to the inventory page after saving
    else:
        form = ProductForm(instance=product)  # Pre-fill the form with the existing product data

    return render(request, 'add_inv.html', {'form': form, 'product': product})