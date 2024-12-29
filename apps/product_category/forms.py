from django import forms
from .models import Product, Category

class ProductFormModel(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug']

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['slug']