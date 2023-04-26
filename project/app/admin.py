from django.contrib import admin
from .models import Category, Products, ProductImages
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display= ['auto_id', 'name', 'description']

class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = ['auto_id', 'category', 'description', 'mrp', 'is_active']

class ProductImagesAdmin(admin.ModelAdmin):
    model = ProductImages
    list_display = ['auto_id', 'product', 'image', 'is_deleted']

admin.site.register(Category, CategoryAdmin)   
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductImages, ProductImagesAdmin) 