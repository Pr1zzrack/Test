from django.db import models
from apps.product_category.models import Product
from django.conf import settings
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers


# Модель корзины
class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")

    def __str__(self):
        return f"{self.user.email}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

# Модель для объектов в корзине
class BasketItem(models.Model):
    cart = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @extend_schema_field(serializers.FloatField)
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.cart.user.email} - {self.product.name}"
    
    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзинах'
