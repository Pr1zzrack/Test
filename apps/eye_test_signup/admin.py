from django.contrib import admin
from .models import SignUpEyeTest


@admin.register(SignUpEyeTest)
class SignUpEyeTestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone_number', 'email')
    search_fields = ('first_name', 'phone_number', 'email')
