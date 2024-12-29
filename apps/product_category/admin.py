from django.contrib import admin
from .models import *
from .forms import ProductFormModel, CategoryModelForm


class ProductModelAdmin(admin.ModelAdmin):
    form = ProductFormModel


class CategoryModelAdmin(admin.ModelAdmin):
    form = CategoryModelForm


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(FormFrame)
admin.site.register(Structure)
admin.site.register(Material)
admin.site.register(Affiliation)
admin.site.register(TempleLength)
admin.site.register(FrameSize)
admin.site.register(SizeBridgeNose)

admin.site.register(Collection)
# admin.site.register(Product)
admin.site.register(ConnectionFilters)
