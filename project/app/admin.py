from django.contrib import admin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display= ['name, description']

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['category', 'description', 'mrp', 'is_active']

class ProductImagesAdmin(admin.ModelAdmin):

    list_display = ['product', 'image', 'is_deleted']