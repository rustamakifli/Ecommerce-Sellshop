from django.db.models.signals import post_save, pre_save
from product.models import Brand, Category, ProductImage, ProductVersion, ProductReview, Product, Color, Size, ProductImage, Tag
from django.dispatch import receiver



@receiver(pre_save, sender = ProductVersion)
def copy_images (sender, instance, **kwargs):
    if not instance.product_images:
        instance.product_images = ProductImage.objects.all().first()
        instance.save()