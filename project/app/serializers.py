from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Category, Products, ProductImages
from .function import generate_auto_id


class CategoryCreateSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(required=False)

    class Meta:
        model=Category
        fields=['auto_id' ,'id', 'name', 'description', 'is_deleted']


class ProductSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(required=False)

    class Meta:
        model=Products
        fields=['auto_id', 'id', 'category', 'description', 'mrp', 'is_active', 'is_deleted']

class ProductImageSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model=ProductImages
        fields=['auto_id', 'id', 'product', 'image', 'is_active', 'is_deleted']
