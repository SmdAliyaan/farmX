from .scraper import scrape_crop_price

def run_scraping_task(crop_name):
    scrape_crop_price(crop_name)
