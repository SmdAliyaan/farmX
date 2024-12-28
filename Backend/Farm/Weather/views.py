from django.shortcuts import render

# Create your views here
from django.http import JsonResponse
from .services.weather_service import fetch_weather
from .services.geolocation import get_city_name

def forecast_view(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    if lat and lon:
        try:
            forecast_data = fetch_weather(lat, lon)
        except Exception as e:
            forecast_data = []  # Handle errors in fetch_weather gracefully
            print(f"Error fetching weather data: {e}")
    else:
        forecast_data = []

    return render(request, 'weather/forecast.html', {
        'forecast': forecast_data
    })

def reverse_geocode(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    city = get_city_name(lat, lon)

    return JsonResponse({'city': city})