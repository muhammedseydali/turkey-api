from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from rest_framework.response import Response
import re
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
import json
from .models import Products, Category, ProductImages 
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer


class Category_add(ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class Product_Add(ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

class ProductImage_Add(ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    permission_classes = (AllowAny,)
    serializer_class = ProductImageSerializer
    queryset = ProductImages.objects.all()