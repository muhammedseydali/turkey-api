import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Basemodel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    creator = models.ForeignKey("auth.User",blank=True,related_name="creator_%(class)s_objects",on_delete=models.CASCADE)
    updater = models.ForeignKey("auth.User",blank=True,null=True,related_name="updater_%(class)s_objects",on_delete=models.CASCADE)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)    
    date_updated = models.DateTimeField(auto_now_add=True)  
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Category(Basemodel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('category')
        ordering = ('name',)

    def __str__(self):
        return "%s" % self.name


class Products(Basemodel):
    name = models.CharField(max_length=255, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    mrp = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(0)])
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        ordering = ('category',)

    def __str__(self):
        return str(self.category)

class ProductImages(Basemodel):
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_image'
        ordering = ('product',)

    def __str__(self):
        return str(self.product)

def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'