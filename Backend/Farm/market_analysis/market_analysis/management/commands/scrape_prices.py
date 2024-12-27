from django.core.management.base import BaseCommand
from market_analysis.scraper import scrape_crop_price

class Command(BaseCommand):
    help = 'Scrape crop prices and predict prices for the next week for a given crop name'

    def add_arguments(self, parser):
        # Add argument to specify the crop name
        parser.add_argument('crop_name', type=str)

    def handle(self, *args, **options):
        crop_name = options['crop_name']
        self.stdout.write(f"Scraping prices and predicting for {crop_name}...")
        
        # Call the scrape_crop_price function to fetch the crop prices and predict the next week's prices
        scrape_crop_price(crop_name)
        
        self.stdout.write(self.style.SUCCESS(f"Successfully scraped and predicted prices for {crop_name}."))
