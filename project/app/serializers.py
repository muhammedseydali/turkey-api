from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Category, Products, ProductImages
from .function import generate_auto_id

class CategorySerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)

    class Meta:
        model=Category
        fields=['auto_id' ,'name', 'description']
    
    def create(self, validated_data):
        creator = self.context['request']
        print(creator, 'creator')
        updater = creator
        auto_id = generate_auto_id(Category)
        return Category.objects.create(creator=creator, updater=updater, auto_id=auto_id, **validated_data)


class ProductSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)

    class Meta:
        model=Products
        fields=['category', 'description', 'mrp', 'is_active']
    
    def create(self, validated_data):
        creator = self.context['user']
        updater = creator
        auto_id = generate_auto_id(Products)
        return Products.objects.create(creator=creator, updater=updater, auto_id=auto_id, **validated_data)


class ProductImageSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model=ProductImages
        fields=['product', 'image', 'is_deleted']

    def create(self, validated_data):
        creator = self.context['user']
        updater = creator
        auto_id = generate_auto_id(ProductImages)
        return ProductImages.objects.create(creator=creator, updater=updater, auto_id=auto_id, **validated_data)


