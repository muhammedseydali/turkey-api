import uuid
from django.db import models

class Basemodel(models.Model):
    auto_id = models.BigAutoField(primary_key=True, editable=False)
    creator = models.CharField(max_length=255)
    updater = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Category(Basemodel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    class Meta:
        db_table = 'category'
        ordering = ('name',)

    def __str__(self):
        return "%s" % self.id


class Products(Basemodel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    mrp = models.TextField(max_length=20)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        ordering = ('category',)

    def __str__(self):
        return str(self.category)

class ProductImages(Basemodel):
    product = models.ForeignKey("Products", limit_choices_to={
                      'is_deleted': False}, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_image'
        ordering = ('product',)

    def __str__(self):
        return str(self.product)