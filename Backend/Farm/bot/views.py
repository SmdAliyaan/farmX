from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from django.conf import settings

@csrf_exempt
def bot(request):
    if request.method == 'POST':
        message = request.POST.get("message", "")
        if message:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            if message.lower() == "hi":
                client.messages.create(
                    from_='whatsapp:+14155238886',  # Twilio WhatsApp sandbox number
                    body=(
                        "Hello,\n\n"
                        "Product Name: Maize 🌽\n"
                        "Expiry Date: Tomorrow, 26-02-2024\n\n"
                        "Product Name: Sorghum 🌱\n"
                        "Expiry Date: Tomorrow, 26-02-2024\n\n"
                        "Product Name: Wheat 🌾\n"
                        "Expiry Date: Tomorrow, 26-02-2024\n\n"
                        "Product Name: Rice 🌾\n"
                        "Expiry Date: Tomorrow, 26-02-2024\n\n"
                        "Please consider using them as soon as possible or think about selling them in the market. Thank you! 🙏🏼"
                    ),
                    to='whatsapp:+919515474144'  # Replace with your verified number
                )
                return HttpResponse("Message sent!")
            else:
                return HttpResponse("Invalid message.")
  
    return render(request, 'bot.html')


def check_expiry():
    today = date.today()
    warning_date = today + timedelta(days=7)  # Set warning threshold
    products = Product.objects.filter(date_expiration__lte=warning_date)

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for product in products:
        message = f"Reminder: The product '{product.name}' is nearing expiry on {product.date_expiration}."
        client.messages.create(
            from_=settings.TWILIO_WHATSAPP_FROM,
            body=message,
            to='whatsapp:+919515474144'  # Replace with actual recipient
        )

