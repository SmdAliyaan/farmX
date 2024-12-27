from twilio.rest import Client
from random import randint
from .models import UserPhone

account_sid = "TWILIO_SID"
auth_token = "TWILIO_AUTH_TOKEN"
twilio_number = "+1234567890"

client = Client(account_sid, auth_token)

def send_verification_code(phone_number):
    otp = str(randint(100000, 999999))
    UserPhone.objects.update_or_create(
        phone_number=phone_number,
        defaults={'otp': otp, 'verified': False}
    )
    client.messages.create(
        body=f"Your FarmX verification code is {otp}.",
        from_=twilio_number,
        to=phone_number
    )

def verify_otp(phone_number, otp):
    try:
        user = UserPhone.objects.get(phone_number=phone_number)
        if user.otp == otp:
            user.verified = True
            user.save()
            return True
        return False
    except UserPhone.DoesNotExist:
        return False

def send_price_alert(phone_number, crop_name, price):
    client.messages.create(
        body=f"Price Alert: {crop_name} is now ₹{price:.2f}.",
        from_=twilio_number,
        to=phone_number
    )
