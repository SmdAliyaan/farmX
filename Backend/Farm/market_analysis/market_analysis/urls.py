from django.urls import path
from .views import register_phone, verify_phone

urlpatterns = [
    path('register/', register_phone, name='register_phone'),
    path('verify/', verify_phone, name='verify_phone'),
]
