from apps.product_category.models import Product
from rest_framework import status
from apps.product_category.tests.test_setup import TestSetup


class ProductAPITests(TestSetup):
    def test_create_product(self):
        data = {"name":"Test Product", "description": "Test description", "price":100, "category": self.category.pk, "stock": 10, "manufacturer":"Test Manufacturer"}
        response = self.client.post(self.product_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_list_product(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_product(self):
        product_id = Product.objects.get(name="Test Product").pk
        response = self.client.get(f"{self.product_url}{product_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Product")
