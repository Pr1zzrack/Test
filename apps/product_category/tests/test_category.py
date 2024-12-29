from apps.product_category.models import Category
from rest_framework import status
from apps.product_category.tests.test_setup import TestSetup


class CategoryAPITests(TestSetup):
    def test_create_category(self):
        data = {"name": "Women", "description": "All Types of Women GlassesTest"}
        response = self.client.post(self.category_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_list_category(self):
        response = self.client.get(self.category_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_category(self):
        category_id = Category.objects.get(name="Test Category").pk
        response = self.client.get(f"{self.category_url}{category_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Category")
