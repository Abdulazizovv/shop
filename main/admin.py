from django.contrib import admin
from .models import Product, Warehouse, SoldProduct, Category

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(SoldProduct)