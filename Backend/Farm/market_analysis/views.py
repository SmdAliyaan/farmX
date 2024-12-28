from django.shortcuts import render
import asyncio
from .scraper import scrape_crop_price
from .predict import predict_prices  # Corrected import

async def price_dashboard(request):
    crop_name = None
    current_price = None
    predicted_price = None
    cities = ["Mumbai", "Delhi"]  # List of cities you want to scrape prices for
    
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name')
        prices = await asyncio.to_thread(scrape_crop_price, crop_name, cities)  # Pass the cities argument
        
        # Only predict if scraping is successful
        if prices:
            predicted_price = sum(prices.values()) // len(prices)  # Mocked average price logic
    
    return render(request, 'market_analysis/price_dashboard.html', {
        'crop_name': crop_name,
        'prices': prices or {},
        'predicted_price': predicted_price
    })
