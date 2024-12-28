from django.urls import path
from . import views

urlpatterns = [
    path('', views.crop_analysis, name='crop_analysis'),
]
