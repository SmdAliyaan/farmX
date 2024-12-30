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
    categories = Category.objects.all()  # Fetch all categories to pass to the template
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Pass the existing product to the form
        if form.is_valid():
            form.save()  # Save the updated product
            return redirect('inventory_report')  # Redirect back to the inventory page after saving
    else:
        form = ProductForm(instance=product)  # Pre-fill the form with the existing product data

    # Pass form, product, and categories to the template
    return render(request, 'add_inv.html', {'form': form, 'product': product, 'categories': categories})






import requests
from django.shortcuts import render

def weather_forecast(request):
    # Initialize empty dictionary for weather data and forecast data
    weather_data = {}
    forecast_data = {}
    city = None  # Initialize city to None
    next_day_forecast = []
    next_week_forecast = []

    # Sample Data for Additional Information for Farmers
    additional_info = {
        "soil_moisture_levels": "Monitoring soil moisture is crucial for optimal crop growth...",
        "crop_planning": "Depending on the rainfall prediction, farmers might opt to plant crops...",
        "pest_management": "Rainfall and humidity can influence pest populations...",
        "water_management": "Efficient water management strategies become essential..."
    }

    if request.method == 'POST':
        city = request.POST.get('city')
    elif request.method == 'GET' and 'city' not in request.GET:
        # Default city if none is provided
        city = 'Hyderabad'  # You can change this to any default city

    if city:
        api_key = '1a5f6c9013c1cf931b5512d06bbdd474'
        
        # Current weather API
        current_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        # 5-day forecast API
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

        try:
            # Get current weather data
            current_response = requests.get(current_url)
            current_response.raise_for_status()  # Check if the request was successful
            current_data = current_response.json()
            
            weather_data = {
                'city': city,
                'temperature': current_data['main']['temp'],
                'description': current_data['weather'][0]['description'],
                'icon': current_data['weather'][0]['icon'],
            }

            # Get forecast data (next 5 days)
            forecast_response = requests.get(forecast_url)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()
            
            # Extract forecast data for the next 24 hours (next day) and next week
            for forecast in forecast_data['list']:
                forecast_time = forecast['dt_txt']
                
                # For next day (midday)
                if "12:00:00" in forecast_time:  
                    next_day_forecast.append({
                        "date": forecast_time.split()[0],
                        "temperature": forecast['main']['temp'],
                        "description": forecast['weather'][0]['description'],
                        "rain": forecast.get('rain', {}).get('3h', 0),
                    })
                
                # For next week (night time, every 3 hours)
                if "00:00:00" in forecast_time:  
                    next_week_forecast.append({
                        "date": forecast_time.split()[0],
                        "temperature": forecast['main']['temp'],
                        "description": forecast['weather'][0]['description'],
                        "rain": forecast.get('rain', {}).get('3h', 0),
                    })
            
        except requests.RequestException:
            weather_data = {'error': 'Error fetching weather data'}

    # Passing actual data to the template
    context = {
        "city": city,
        "weather_data": weather_data,
        "next_day_forecast": next_day_forecast,
        "next_week_forecast": next_week_forecast,
        "additional_info": additional_info,
    }
    
    return render(request, 'weather_forecast.html', context)
