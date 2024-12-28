from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prices/<str:crop>/', views.get_crop_prices, name='get_crop_prices'),
    path('predict/<str:crop>/', views.predict_prices, name='predict_prices'),
]
