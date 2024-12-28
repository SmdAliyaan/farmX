from django.urls import path
from . import views

urlpatterns = [
    path('forecast/', views.forecast_view, name='forecast'),
    path('reverse-geocode/', views.reverse_geocode, name='reverse_geocode'),
]