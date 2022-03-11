from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    parent_cat = models.ForeignKey(Self, related_name='mysweetchild', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    info = models.TextField()


class PropertyName(models.Model):
    category = models.ForeignKey(Category, related_name='propertyname', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class PropertyValues(models.Model):
    property_name = models.ForeignKey(PropertyName, related_name='propertyvalue', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class ProductVersion(models.Model):
    publications = models.ManyToManyField(PropertyValues)
    product = models.ForeignKey(Product, related_name='productchild', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    is_main = models.BooleanField()

class ProductImages(models.Model):
    product_version = models.ForeignKey(ProductVersion, related_name='productimage', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/story_images/')
    is_main = models.BooleanField()


class ProductReviews(models.Model):
    user = models.ForeignKey(User, related_name='productreview1', on_delete=models.CASCADE)
    product_version = models.ForeignKey(ProductVersion, related_name='productreview2', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    info = models.TextField()


class Brand(models.Model):
    product = models.ForeignKey(Product, related_name='brand', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


print("test")