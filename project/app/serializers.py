from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Category
        fields=['name', 'description']