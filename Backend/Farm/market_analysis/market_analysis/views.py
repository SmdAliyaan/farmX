from django.shortcuts import render, redirect
from django.http import JsonResponse
from .sms import send_verification_code, verify_otp
from .models import UserPhone

def register_phone(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        send_verification_code(phone_number)
        return JsonResponse({'message': 'OTP sent to your phone.'})

def verify_phone(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        otp = request.POST.get('otp')
        if verify_otp(phone_number, otp):
            return JsonResponse({'message': 'Phone verified successfully.'})
        else:
            return JsonResponse({'error': 'Invalid OTP. Try again.'})
