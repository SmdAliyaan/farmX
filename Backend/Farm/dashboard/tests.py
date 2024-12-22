from django.test import TestCase

# Create your tests here.
@login_required
def dashboard(request):
    # Get stats for the last 30 days
    thirty_days_ago = timezone.now().date() - timedelta(days=30)
    stats = DashboardStats.objects.filter(date__gte=thirty_days_ago)
    
    context = {
        'total_users': stats.latest('date').total_users if stats.exists() else 0,
        'active_users': stats.latest('date').active_users if stats.exists() else 0,
        'monthly_revenue': stats.aggregate(Sum('revenue'))['revenue__sum'] or 0,
        'monthly_orders': stats.aggregate(Sum('orders'))['orders__sum'] or 0,
        'daily_stats': stats.values('date', 'revenue', 'orders'),
    }
    return render(request, 'dashboard/index.html', context)

# In urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]