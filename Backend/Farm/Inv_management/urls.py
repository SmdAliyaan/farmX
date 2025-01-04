from django.urls import path
from . import views
from .views import weather_forecast,gemini,generate_pdf
urlpatterns = [
    path('', views.inventory_report, name='inventory_report'),
    path('add/', views.add_product, name='add_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
     path('edit/<int:pk>/', views.edit_product, name='edit_product'),
      path('weather', weather_forecast, name='weather_forecast'),
       path('generate_pdf', generate_pdf, name='generate_pdf'),
    path('gemini', gemini, name='gemini'),
     ]
