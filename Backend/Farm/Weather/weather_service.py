

import requests
import os

WEATHER_API_KEY = os.getenv('59184731d4294058aac73937242812')  # Securely load your API key from .env

def fetch_weather(lat, lon):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={lat},{lon}&days=7"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        forecast_data = []
        
        for day in data['forecast']['forecastday']:
            forecast_data.append({
                'date': day['date'],
                'temp_day': day['day']['avgtemp_c'],
                'temp_night': day['day']['mintemp_c'],
                'weather': day['day']['condition']['text'],
                'icon': day['day']['condition']['icon']
            })
        
        return forecast_data
    else:
        return []