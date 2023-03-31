from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
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
from .serializers import CategorySerializer 


class Category_add(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
