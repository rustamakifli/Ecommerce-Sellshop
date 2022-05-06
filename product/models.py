from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    parent_cat = models.ForeignKey('self', related_name='mysweetchild', on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    
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
        verbose_name_plural = 'Property names'

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
    product = models.ForeignKey(Product, related_name='product_product_version', on_delete=models.CASCADE, default=1, null=True, blank=True)
    title = models.CharField(max_length=50)
    property=models.ManyToManyField(PropertyValues,blank=True)
    old_price = models.DecimalField(decimal_places = 2 ,max_digits=6,null=True,blank=True)
    new_price = models.DecimalField(decimal_places = 2 ,max_digits=6)
    quantity = models.IntegerField(null=True,blank=True)
    description = models.TextField()
    featured = models.BooleanField(default=False)

    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'Product version'
        verbose_name_plural = 'Product versions'

    def __str__(self):
        return self.title

    def is_featured(self):
        return self.featured

class ProductImages(models.Model):
    product_version = models.ForeignKey(ProductVersion, related_name='product_image', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='story_images/',  null = True , blank = True)
    is_main = models.BooleanField('main pic', default=False)
    image_title = models.CharField('Image title' , max_length=100 , null=True)
    
    def __str__(self):
        return str(self.image_title)
        #  + ' ' + self.product_version.title + ' ' + self.product_version.new_price

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = 'Product images'


class ProductReviews(AbsrtactModel):
    product_version = models.ForeignKey(ProductVersion, related_name='product_review', on_delete=models.CASCADE, default=1)
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
