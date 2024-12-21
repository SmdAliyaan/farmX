# # Inv_management/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.inventory_report, name='inventory_report'),  
# ]
# urls.py

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_report, name='inventory_report'),
    path('add/', views.add_product, name='add_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]