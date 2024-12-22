from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.core.mail import send_mail
from . import views
from .views import ind, registration_view




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('inv/', include('Inv_management.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", ind, name="index"),
    path("accounts/register/", registration_view, name="register"),
    path('dash/', include('dashboard.urls')),

   

]