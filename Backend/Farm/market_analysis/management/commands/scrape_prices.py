from django.core.management.base import BaseCommand
from models import CropPrice
from scraper import scrape_crop_price
from datetime import date

CROPS = ['wheat', 'rice', 'maize', 'barley']

class Command(BaseCommand):
    help = 'Scrape crop prices and save to database'

    def handle(self, *args, **kwargs):
        for crop in CROPS:
            price = scrape_crop_price(crop)
            if price:
                CropPrice.objects.create(
                    crop_name=crop,
                    price=price,
                    date=date.today()
                )
                self.stdout.write(self.style.SUCCESS(f'Success: {crop} - ₹{price}'))
            else:
                self.stdout.write(self.style.WARNING(f'Failed: {crop}'))
