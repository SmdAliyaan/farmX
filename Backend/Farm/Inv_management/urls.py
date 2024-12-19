# Inv_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_report, name='inventory_report'),  
]
