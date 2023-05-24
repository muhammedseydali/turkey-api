from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Category, Products, ProductImages
from .function import generate_auto_id


class DeletImageSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()

    class Meta:
        model = ProductImages
        fields = ('id')

class CategoryCreateSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(required=False)

    class Meta:
        model=Category
        fields=['auto_id' ,'id', 'name', 'description', 'is_deleted']

class ProductSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(required=False)
    image = serializers.ImageField(max_length = None, allow_empty_file=False, use_url = True)

    class Meta:
        model=Products
        fields=['auto_id', 'id', 'category', 'description', 'mrp', 'image', 'is_active', 'is_deleted']
    

class ProductRetrieveSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(required=False)
    image = serializers.ImageField(max_length = None, allow_empty_file=False, use_url = True)

    class Meta:
        model=Products
        fields=['auto_id', 'id', 'category', 'description', 'mrp', 'image', 'is_active', 'is_deleted']
    
    def get_image(self, instance):
        request = self.context['request']
        image_url = instance.image.image.url
        return request.build_absolute_uri(image_url)

class ProductImageSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    product = ProductSerializer(read_only=True)
    image = serializers.ImageField(max_length=None, use_url = True)

    class Meta:
        model=ProductImages
        fields=['auto_id', 'id', 'product', 'image', 'is_deleted']

    def create(self, validated_data):
        creator = self.context['user']
        updater = self.context['user']
        auto_id = generate_auto_id(ProductImages)
        return ProductImages.objects.create(creator=creator, updater=updater, auto_id=auto_id, **validated_data)
