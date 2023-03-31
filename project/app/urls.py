from django.urls import path
from . import views
from .views import Category_add
from django.urls import path, re_path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', Category_add)


app_name = "app"


urlpatterns = router.urls

