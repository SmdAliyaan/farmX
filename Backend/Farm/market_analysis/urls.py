from django.urls import path
from .views import price_dashboard

urlpatterns = [
    path('', price_dashboard, name='price_dashboard'),
]