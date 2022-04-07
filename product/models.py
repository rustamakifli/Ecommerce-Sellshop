from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    parent_cat = models.ForeignKey('self', related_name='mysweetchild', on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category_product', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=30)
    info = models.TextField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class PropertyName(models.Model):
    category = models.ForeignKey(Category, related_name='category_property_name', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Property name'
        verbose_name_plural = 'Propert names'

    def __str__(self):
        return self.name

class PropertyValues(models.Model):
    property_name = models.ForeignKey(PropertyName, related_name='property_name_property_value', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Property values'
        verbose_name_plural = 'Property values'

    def __str__(self):
        return self.name

class ProductVersion(models.Model):
    publications = models.ManyToManyField(PropertyValues)
    product = models.ForeignKey(Product, related_name='product_product_version', on_delete=models.CASCADE, default=1, null=True, blank=True)
    title = models.CharField(max_length=50)
    old_price = models.DecimalField(decimal_places = 2 ,max_digits=6,null=True,blank=True)
    new_price = models.DecimalField(decimal_places = 2 ,max_digits=6)
    quantity = models.IntegerField(null=True,blank=True)
    description = models.TextField()
    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'Product version'
        verbose_name_plural = 'Product versions'

    def __str__(self):
        return self.title

class ProductImages(models.Model):
    product_version = models.ForeignKey(ProductVersion, related_name='product_image', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='story_images/')
    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'Product images'
        verbose_name_plural = 'Product images'

    # def __str__(self):
    #     return self.image

class ProductReviews(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    review = models.TextField()

    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product reviews'

    def __str__(self):
        return self.name


class Brand(models.Model):
    product = models.ForeignKey(Product, related_name='product_brand', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title
