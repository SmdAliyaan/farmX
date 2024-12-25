from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ind, registration_view
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('inv/', include('Inv_management.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", ind, name="index"),
    path("accounts/register/", registration_view, name="register"),
    path('dash/', include('dashboard.urls')),
    path('bot/', include('bot.urls'))
]
