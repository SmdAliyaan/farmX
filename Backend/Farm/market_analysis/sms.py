from twilio.rest import Client
from random import randint
from .models import UserPhone

account_sid = "ACe878110ff7ee0b1c6fd6754019ea71b2"
auth_token = "2df008d871bdd1acda99bae50b27c0dc"
twilio_number = "+14155238886"  # Ensure this is a valid Twilio number associated with your account
your_number = "+919515474144"  # Your number

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
        to=your_number  # Always send to your number
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
        to=your_number  # Always send to your number
    )