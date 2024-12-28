# views.py

import asyncio
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import time

URL = 'https://www.agriculturemarket.com/today-prices'

# Function to scrape crop prices
def scrape_crop_price(crop_name, cities, retries=3):
    prices = {}
    for city in cities:
        url = f"https://www.agriwatch.com"  # Replace with the actual URL of the crop prices
        attempt = 0
        while attempt < retries:
            try:
                response = requests.get(url, timeout=10)  # Added timeout to avoid hanging requests
                response.raise_for_status()  # Raises an HTTPError if status code >= 400
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Example: Look for a price in a specific element (replace with actual logic)
                price_element = soup.find("span", {"class": "price"})
                if price_element:
                    price = price_element.text.strip()
                    prices[city] = price
                    break  # Exit loop on successful scrape
                else:
                    prices[city] = None  # Price not found
                    break

            except requests.exceptions.Timeout:
                print(f"Timeout error for {city}. Retrying... ({attempt + 1}/{retries})")
            except requests.exceptions.RequestException as e:
                print(f"Failed to scrape {crop_name} price for {city}: {e}")
                prices[city] = None
                break  # Stop retrying on other request errors
            
            attempt += 1
            time.sleep(2)  # Wait before retrying
        if attempt == retries:
            print(f"Failed to get data for {city} after {retries} retries.")
            prices[city] = None  # If retry limit is reached, set to None
    return prices

# Django view to handle the price dashboard
async def price_dashboard(request):
    crop_name = "wheat"  # Example crop name, can be dynamic as needed
    cities = ["Mumbai", "Delhi"]  # List of cities you want to scrape prices for

    # Call the scraping function, passing both crop_name and cities
    prices = await asyncio.to_thread(scrape_crop_price, crop_name, cities)

    # Render the prices in the template
    return render(request, 'market_analysis/price_dashboard.html', {'prices': prices})
