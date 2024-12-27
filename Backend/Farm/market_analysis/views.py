from django.shortcuts import render, redirect
from django.http import JsonResponse
from .sms import send_verification_code, verify_otp
from .models import UserPhone
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def register_phone(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        send_verification_code(phone_number)
        return redirect(f"{reverse('verify_phone')}?phone={phone_number}")
    return render(request, 'market_analysis/register_market.html')

def verify_phone(request):
    phone_number = request.GET.get('phone')
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        otp = request.POST.get('otp')
        if verify_otp(phone_number, otp):
            return redirect('market_landing')
        else:
            return render(request, 'market_analysis/verify.html', {'phone': phone_number, 'error': 'Invalid OTP. Try again.'})
    return render(request, 'market_analysis/verify.html', {'phone': phone_number})

def market_landing(request):
    return render(request, 'market_analysis/market_landing.html')
