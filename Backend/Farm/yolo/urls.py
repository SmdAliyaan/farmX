# urls.py in your Django app

from django.urls import path
from .views import out_of_stock  # Import the required view

urlpatterns = [
    path('out-of-stock/', out_of_stock, name='out_of_stock'),  # Use consistent URL patterns
]
