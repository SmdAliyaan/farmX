from django.contrib import admin
from django.urls import path, include
from .views import chat_with_ai
from . import views
from .views import order_view

app_name = 'resources'
urlpatterns = [
    path('chat_with_ai', chat_with_ai, name='chat_with_ai'),
   path('order/', order_view, name='order'),

path('resource-estimation/', views.chat_with_ai, name='resource_estimation'),
    
]