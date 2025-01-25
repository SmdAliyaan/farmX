# from django.test import TestCase
# from Inv_management.models import Product, Category, Farmer
# from datetime import date, timedelta

# def create_test_data():
#     # Create test farmer
#     farmer = Farmer.objects.create(
#         name="Test Farmer",
#         phone_number="+1234567890"  # Replace with your WhatsApp number
#     )
    
#     # Create test category
#     category = Category.objects.create(name="Test Category")
    
#     # Create products expiring tomorrow
#     Product.objects.create(
#         name="Test Product 1",
#         price=10.00,
#         quantity_total=10,
#         quantity_remaining=5,
#         date_bought=date.today(),
#         date_expiration=date.today() + timedelta(days=1),
#         category=category,
#         farmer=farmer
#     )

# # Run in Django shell
# python manage.py shell
# >>> from bot.tests import create_test_data
# >>> create_test_data()
