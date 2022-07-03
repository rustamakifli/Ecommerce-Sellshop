from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy



User = get_user_model()


class Category(models.Model):
    parent_cat = models.ForeignKey('self', related_name='sub_categories', on_delete=models.CASCADE, null=True, blank=True, default="",)
    title = models.CharField(max_length=50, db_index=True)
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    
    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='brand_products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def is_featured(self):
        return self.featured

    @property
    def main_version(self):
        return self.product_versions.filter(is_main=True).first()


class ProductVersion(models.Model):
    title = models.CharField(max_length=100, db_index=True,)
    product = models.ForeignKey(Product, related_name='product_versions', on_delete=models.CASCADE, null=True, default=1, blank=True)
    color = models.ForeignKey(Color, related_name='same_color_product_versions', on_delete=models.CASCADE, default=1)
    size = models.ForeignKey(Size, related_name='same_size_product_versions', on_delete=models.CASCADE, null=True, blank=True)
    old_price = models.DecimalField(decimal_places = 2, max_digits=6, null=True, blank=True, default=0)
    new_price = models.DecimalField(decimal_places = 2, max_digits=6)
    quantity = models.PositiveIntegerField(default=0)
    is_main = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not self.quantity:
            self.title = f'{self.product.title} {self.color} (Out of Stock)'
        else:
            self.title = f'{self.product.title} {self.color}'

    def get_absolute_url(self):
        return f"/products/{self.id}/"

    class Meta:
        verbose_name = 'Product version'
        verbose_name_plural = 'Product versions'

    def __str__(self):
        return self.title

    def main_image(self):
        return self.product_images.all().order_by('is_main').first()

    def other_images(self):
        return self.product_images.all().exclude('is_main')




class ProductImage(models.Model):
    product_version = models.ForeignKey(ProductVersion, related_name='product_images', on_delete=models.CASCADE, default=1)
    image = models.FileField(upload_to='product_images',  null = True , blank = True)
    is_main = models.BooleanField('Main picture', default=False)
    
    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = 'Product images'

    


class ProductReview(models.Model):
    CHOICES = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )

    product_version = models.ForeignKey(ProductVersion, related_name='product_reviews', on_delete=models.CASCADE, default="1", null=True)
    user = models.ForeignKey(User, related_name='user_product_reviews', on_delete=models.CASCADE, editable=False, default="1")
    review = models.TextField()
    rating = models.IntegerField(choices=CHOICES, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product reviews'


    def __str__(self):
        return f"{self.review}-{self.rating}-{self.user.username}"



