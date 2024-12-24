import requests
from django.shortcuts import render
from django.conf import settings

def map_view(request):
    api_key = settings.OPENWEATHER_API_KEY
    default_lat, default_lon = 40.7128, -74.0060  # New York as default
    
    if request.GET.get('lat') and request.GET.get('lon'):
        lat = request.GET['lat']
        lon = request.GET['lon']
    else:
        lat, lon = default_lat, default_lon
    
    weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&units=metric&appid={api_key}"
    response = requests.get(weather_url).json()

    forecast = response.get('daily', [])

    return render(request, 'map.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'forecast': forecast,
        'lat': lat,
        'lon': lon,
    })
