

import requests
import os 

GOOGLE_API_KEY = os.getenv('AIzaSyBa_Y-FgWP9YDOHde_1Rz0MVMl_Z8L5wDY')  # Google Maps API Key

def get_city_name(lat, lon):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        for component in data['results'][0]['address_components']:
            if 'locality' in component['types']:
                return component['long_name']
    return 'Unknown'