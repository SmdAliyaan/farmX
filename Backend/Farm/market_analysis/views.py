from django.shortcuts import render
import asyncio
from .scraper import get_crop_prices_from_csv
from .predict import predict_prices  # Corrected import

async def price_dashboard(request):
    crop_name = None
    current_price = None
    predicted_price = None
    prices = {}  # Initialize prices to an empty dictionary
    
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name')
        prices = await asyncio.to_thread(get_crop_prices_from_csv, crop_name)  # Pass the crop name
        
        # Only predict if scraping is successful
        if prices:
            predicted_price = sum(prices.values()) // len(prices)  # Mocked average price logic
    
    return render(request, 'market_analysis/price_dashboard.html', {
        'crop_name': crop_name,
        'prices': prices,
        'predicted_price': predicted_price
    })
