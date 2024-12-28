# views.py
from django.shortcuts import render
from Weather.geolocation import get_city_name  # Corrected import
from Weather.weather_service import fetch_weather  # Corrected import

def map_view(request):
    # Default coordinates (fallback to a specific city if user location isn't provided)
    default_lat, default_lon = 12.9716, 77.5946  # Bengaluru, for example

    # Get coordinates from the request
    lat = request.GET.get('lat', default_lat)
    lon = request.GET.get('lon', default_lon)

    # Convert to float
    lat, lon = float(lat), float(lon)

    # Get city name using coordinates
    city_name = get_city_name(lat, lon)

    # Fetch 7-day weather forecast
    forecast = fetch_weather(lat, lon)

    return render(request, 'forecast/map.html', {
        'lat': lat,
        'lon': lon,
        'forecast': forecast,
        'city_name': city_name,
    })
