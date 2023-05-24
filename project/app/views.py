
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Products, Category, ProductImages 
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q
from .serializers import CategoryCreateSerializer, ProductSerializer, ProductImageSerializer,ProductRetrieveSerializer
from .function import generate_auto_id

from rest_framework.decorators import action
from rest_framework.response import Response


class Category_add(ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    permission_classes = (AllowAny,)
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()

    def get_serializer_context(self):
        return {
            'request':self.request,
            'user':self.request.user
        }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        creator = request.user
        updater = creator
        category = Category.objects.create(creator=creator, updater=updater, auto_id=generate_auto_id(Category), **serializer.validated_data)
        return Response(CategoryCreateSerializer(category).data)

class Product_Add(ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_serializer_context(self):
        return {
            'request':self.request,
            'user':self.request.user
        }
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return ProductSerializer
        return ProductRetrieveSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        creator = request.user
        updater = creator
        product = Products.objects.create(creator=creator, updater=updater, auto_id=generate_auto_id(Products), **serializer.validated_data)
        return Response(ProductSerializer(product).data)


    
class ProductImage_Add(ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    permission_classes = (AllowAny,)
    serializer_class = ProductImageSerializer
    queryset = ProductImages.objects.all()

    def get_serializer_context(self):
        return {
            'request':self.request,
            'user':self.request.user
        }
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        creator = request.user
        updater = creator
        product_images = ProductImages.objects.create(creator=creator, updater=updater, auto_id=generate_auto_id(ProductImages), **serializer.validated_data)
        return Response(ProductSerializer(product_images).data)
    