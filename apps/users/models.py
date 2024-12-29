from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta
import random
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Пользователь должен иметь email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True) # Электронная почта пользователя
    is_active = models.BooleanField(default=True) # Статус активации аккаунта
    is_staff = models.BooleanField(default=False) # Статус доступа к админ панели

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Пользователь
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True) # фото профиля пользователя
    first_name = models.CharField(max_length=50, blank=True, null=True) # Имя пользователя
    last_name = models.CharField(max_length=50, blank=True, null=True) # фамилия пользователя
    address = models.CharField(max_length=100, blank=True, null=True) # Адрес пользователя
    date_of_birth = models.DateField(null=True, blank=True) # Дата рождения пользователя
    gender = models.CharField(max_length=10, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], null=True, blank=True) # Пол пользователя

    def __str__(self):
        return f"{self.user.email} профиль"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class EmailConfirmation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Пользователь
    code = models.CharField(max_length=6) # Код активации
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания аккаунта

    def __str__(self):
        return f'Код для пользователя: {self.user.email}'
    
    def is_expired(self):
        return now() > self.created_at + timedelta(minutes=10)

    @staticmethod
    def generate_code():
        return ''.join(random.choices('0123456789', k=6))

    class Meta:
        verbose_name = 'Код активации Аккаунта'
        verbose_name_plural = 'Коды активации Аккаунта'
