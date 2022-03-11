from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    parent_cat = models.ForeignKey('self', related_name='category_sub_cat', on_delete=models.CASCADE, default=1, null=True, blank=True)
    title = models.CharField(max_length=50)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category_product', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=30)
    info = models.TextField()


class PropertyName(models.Model):
    category = models.ForeignKey(Category, related_name='category_property_name', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)


class PropertyValues(models.Model):
    property_name = models.ForeignKey(PropertyName, related_name='property_name_property_value', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)


class ProductVersion(models.Model):
    publications = models.ManyToManyField(PropertyValues)
    product = models.ForeignKey(Product, related_name='product_product_version', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    is_main = models.BooleanField()


class ProductImages(models.Model):
    product_version = models.ForeignKey(ProductVersion, related_name='product_image', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='media/story_images/')
    is_main = models.BooleanField()


class ProductReviews(models.Model):
    user = models.ForeignKey(User, related_name='user_product_review', on_delete=models.CASCADE, default=1)
    product_version = models.ForeignKey(ProductVersion, related_name='production_version_product_review', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=30)
    info = models.TextField()


class Brand(models.Model):
    product = models.ForeignKey(Product, related_name='product_brand', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)

