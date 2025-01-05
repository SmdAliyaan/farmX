from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from datetime import date, timedelta
from Inv_management.models import Product, Farmer
import logging
import schedule
import time
import threading

# Direct Twilio credentials instead of settings
client = Client('ACe878110ff7ee0b1c6fd6754019ea71b2', '2df008d871bdd1acda99bae50b27c0dc')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def check_expiring_products():
    try:
        today = date.today()
        tomorrow = today + timedelta(days=1)
        logger.info(f"Checking products expiring on {tomorrow}")  # Debug log

        expiring_products = Product.objects.filter(
            date_expiration=tomorrow,
            quantity_remaining__gt=0
        )
        logger.info(f"Found {expiring_products.count()} expiring products")  # Debug log

        if expiring_products:
            message = "⚠️ Products Expiring Tomorrow:\n\n"
            for product in expiring_products:
                message += (
                    f"⦿ Name: {product.name}\n"
                    f"Quantity: {product.quantity_remaining}\n"
                    f"Expiry Date: {product.date_expiration}\n\n"
                )

            logger.info(f"Attempting to send message: {message}")  # Debug log

            # Send WhatsApp message
            try:
                response = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=message,
                    to='whatsapp:+919515474144'  # Format for WhatsApp
                )
                logger.info(f"Message sent successfully. SID: {response.sid}")
            except Exception as e:
                logger.error(f"Error sending message: {str(e)}")
                logger.error(f"Twilio Error: {e}")

        else:
            logger.info("No products expiring tomorrow")
    except Exception as e:
        logger.error(f"Error in check_expiring_products: {str(e)}")

def schedule_checker():
    # schedule.every(1).minutes.do(check_expiring_products)
    schedule.every().day.at("07:30").do(check_expiring_products)
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start the scheduler in a background thread
checker_thread = threading.Thread(target=schedule_checker)
checker_thread.daemon = True
checker_thread.start()

@csrf_exempt
def bot(request):
    if request.method == 'POST':
        message = request.POST.get("message", "")
        if message and message.lower() == "hi":
            check_expiring_products()
            return HttpResponse("Checking expiring products...")
    return render(request, 'bot.html')