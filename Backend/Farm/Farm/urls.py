
# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('about/', views.about, name='about'),
#     path('inv/', include('Inv_management.urls')),
#     path('', views.home, name='home')
#     path('', include(("base.urls","base"), "base"))
# ]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('inv/', include('Inv_management.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    
    
]