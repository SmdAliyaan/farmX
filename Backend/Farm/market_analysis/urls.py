from django.urls import path
from .views import market_landing, register_phone, verify_phone

urlpatterns = [
    path('', market_landing, name='market_landing'),
    path('register/', register_phone, name='register_phone'),
    path('verify/', verify_phone, name='verify_phone'),
]