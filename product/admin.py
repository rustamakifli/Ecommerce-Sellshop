from django.contrib import admin

# Register your models here.

from product.models import Category, Product, ProductImages, ProductPropertyValues, ProductReviews, ProductVersion, PropertyName, PropertyValues, Brand

admin.site.register([Category, Product, ProductImages, ProductPropertyValues, ProductReviews, ProductVersion, PropertyName, PropertyValues, Brand])