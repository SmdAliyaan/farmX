from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from datetime import date, timedelta
from Inv_management.models import Product, Farmer
import logging

# Direct Twilio credentials instead of settings
client = Client('ACe878110ff7ee0b1c6fd6754019ea71b2', '2df008d871bdd1acda99bae50b27c0dc')

logger = logging.getLogger(__name__)

def check_expiring_products():
    try:
        today = date.today()
        tomorrow = today + timedelta(days=1)
        print(f"Checking products expiring on {tomorrow}")  # Debug print

        expiring_products = Product.objects.filter(
            date_expiration=tomorrow,
            quantity_remaining__gt=0
        )
        print(f"Found {expiring_products.count()} expiring products")  # Debug print

        if expiring_products:
            for product in expiring_products:
                try:
                    message = (
                        f"⚠️ Product Expiring Tomorrow!\n"
                        f"Name: {product.name}\n"
                        f"Quantity: {product.quantity_remaining}"
                    )

                    print(f"Attempting to send message: {message}")  # Debug print

                    # Send WhatsApp message
                    response = client.messages.create(
                        from_='whatsapp:+14155238886',
                        body=message,
                        to='whatsapp:+919515474144'  # Format for WhatsApp
                    )
                    print(f"Message sent successfully. SID: {response.sid}")

                except Exception as e:
                    print(f"Error sending message: {str(e)}")
        else:
            print("No products expiring tomorrow")
    except Exception as e:
        print(f"Error in check_expiring_products: {str(e)}")

@csrf_exempt
def bot(request):
    if request.method == 'POST':
        message = request.POST.get("message", "")
        if message and message.lower() == "hi":
            check_expiring_products()
            return HttpResponse("Checking expiring products...")
    return render(request, 'bot.html')