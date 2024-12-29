# urls.py in your Django app

from django.urls import path
from .views import out_of_stock  # Import the required view
from .views import start_detection

urlpatterns = [
    path('out-of-stock/', out_of_stock, name='out_of_stock'), 
     path('start-detection/', start_detection, name='start_detection'), # Use consistent URL patterns
]
