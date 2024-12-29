from dirtyfields import DirtyFieldsMixin
from django.db import models


class SignUpEyeTest(models.Model):
    first_name = models.CharField(max_length=30) # Имя пользователя
    phone_number = models.CharField(max_length=18) # номер телефона пользователя
    email = models.EmailField() # Электронная почта пользователя
    comment = models.TextField() # Комментарий от пользователя
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания
    updated_at = models.DateTimeField(auto_now=True) # Дата последнего обновления 

    def __str__(self):
        return f"{self.first_name} - {self.phone_number} - {self.created_at}"
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
