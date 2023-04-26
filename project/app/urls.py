from django.urls import path
from . import views
from .views import Category_add, Product_Add, ProductImage_Add
from django.urls import path, re_path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', Category_add)
router.register(r'product', Product_Add)
router.register(r'image', ProductImage_Add)

app_name = "app"


urlpatterns = [
    path('', include(router.urls))
]

