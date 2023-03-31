import uuid
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    creator = models.ForeignKey("auth.User",blank=True,related_name="creator_%(class)s_objects",on_delete=models.CASCADE)
    updater = models.ForeignKey("auth.User",blank=True,null=True,related_name="updater_%(class)s_objects",on_delete=models.CASCADE)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)    
    date_updated = models.DateTimeField(auto_now_add=True)  
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    class Meta:
        db_table = 'category'
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.auto_id)


class Products(BaseModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    mrp = models.TextField(max_length=20)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.auto_id)

class ProductImages(BaseModel):
    product = models.ForeignKey("Products", limit_choices_to={
                      'is_deleted': False}, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_image'
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.auto_id)