from django.shortcuts import render
from .scraper import scrape_crop_price
from .tasks import predict_price
from datetime import datetime

def price_dashboard(request):
    crop_name = None
    current_price = None
    predicted_price = None
    
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name')
        current_price = scrape_crop_price(crop_name)
        
        # Only predict if scraping is successful
        if current_price:
            predicted_price = predict_price(crop_name)
    
    return render(request, 'price_dashboard.html', {
        'crop_name': crop_name,
        'current_price': current_price,
        'predicted_price': predicted_price
    })
