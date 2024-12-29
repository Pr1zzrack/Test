from rest_framework.test import APITestCase
from apps.product_category.models import Category, Product


class TestSetup(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="Test description")
        self.product = Product.objects.create(name="Test Product", description="Test description", price=100, category=self.category, stock=10, manufacturer="Test Manufacturer")
        self.product_url = "/api/products/"
        self.category_url = "/api/categories/"