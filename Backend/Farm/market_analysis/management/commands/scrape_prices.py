from django.core.management.base import BaseCommand
from market_analysis.scraper import scrape_crop_price  # Importing from market_analysis.scraper
from datetime import date
from market_analysis.models import CropPrice

CROPS = ['wheat', 'rice', 'maize', 'barley']
CITIES = ['Mumbai', 'Delhi']

class Command(BaseCommand):
    help = 'Scrape crop prices and save to database'

    def handle(self, *args, **kwargs):
        for crop in CROPS:
            prices = scrape_crop_price(crop, cities=CITIES)
            if prices:
                for city, price in prices.items():
                    # Check if the price is None, set to 0 if missing
                    if price is None:
                        price = 0  # Default value if price not found

                    # Save the scraped data into CropPrice model
                    CropPrice.objects.create(
                        crop_name=crop,
                        market=city,
                        price=price,
                        date=date.today()
                    )
                    self.stdout.write(self.style.SUCCESS(f'Success: {crop} ({city}) - ₹{price}'))
            else:
                self.stdout.write(self.style.WARNING(f'Failed: {crop}'))

