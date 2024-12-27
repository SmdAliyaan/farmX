from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('inv/', include('Inv_management.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.ind, name="index"),
    path("accounts/register/", views.registration_view, name="register"),
    path('dash/', include('dashboard.urls')),
    path('bot/', include('bot.urls')),
    path('test/', views.test, name='test'),  # Ensure this line is correct
]
