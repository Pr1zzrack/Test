from django.db import models
from ..product_category.models import Product


class Order(models.Model):
    name = models.CharField(max_length=30) # Имя
    phone = models.CharField(max_length=20) # Номер телефона пользователя
    address_and_comment = models.TextField() # Адрес и коментарий
    delivery_method = models.CharField(max_length=13, choices=[('яндекс такси', 'Яндекс Такси'), ('самовывоз', 'Самовывоз')]) # Способ доставки
    payment_method = models.CharField(max_length=16, choices=[('банковская карта', 'Банковская карта'), ('наличные', 'Наличные')]) # Способ оплаты
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания
    updated_at = models.DateTimeField(auto_now=True) # Дата последнего обновления 

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.payment_method} - {self.created_at}"
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
