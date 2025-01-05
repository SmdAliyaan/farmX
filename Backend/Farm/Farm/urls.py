from django.conf import settings
from django.conf.urls.static import static
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
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),  # Keep this one
    path('bot/', include('bot.urls')),
    path('test/', views.test, name='test'),
    path('plant/', include('plant.urls')),
    path('app/', include('myapp.urls')),
    
    path('resources/', include('resources.urls', namespace='resources')),
    path('order/', views.order_view, name='order'),
    path('marketplace/', include('inventory_recommendation.urls')),
]


# Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

