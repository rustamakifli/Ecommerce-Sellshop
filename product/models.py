from django.db import models


class Category(models.Model):
    # parent_cat_id = models.ForeignKey(Category, related_name='mysweetchild', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


class Product(models.Model):
    # category_id = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    info = models.TextField()


class ProductVersion(models.Model):
    # product_id = models.ForeignKey(Product, related_name='productchild', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    is_main = models.BooleanField()


class PropertyName(models.Model):
    # category_id = models.ForeignKey(Category, related_name='propertyname', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class PropertyValues(models.Model):
    # property_name_id = models.ForeignKey(PropertyName, related_name='propertyvalue', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class ProductPropertyValues(models.Model):
    # product_version_id = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    # property_values_id = models.ForeignKey(PropertyValues, related_name='propertyvalues', on_delete=models.CASCADE)
    pass


class ProductImages(models.Model):
    # product_version_id = models.ForeignKey(ProductVersion, related_name='productimage', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/story_images/')
    is_main = models.BooleanField()


class ProductReviews(models.Model):
    # user_id = models.ForeignKey(User, related_name='productreview1', on_delete=models.CASCADE)
    # product_version_id = models.ForeignKey(ProductVersion, related_name='productreview2', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    info = models.TextField()


class Brand(models.Model):
    # product_id = models.ForeignKey(Product, related_name='brand', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


