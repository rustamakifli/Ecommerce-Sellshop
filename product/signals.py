from django.db.models.signals import post_save, pre_save
from product.models import Brand, Category, ProductImage, ProductVersion, ProductReview, Product, Color, Size, ProductImage, Tag
from django.dispatch import receiver



# @receiver(pre_save, sender = ProductVersion)
# def copy_images (sender, instance, **kwargs):
#     if not instance.product_images:
#         instance.product_images = ProductImage.objects.all().first()
#         instance.save()


@receiver(pre_save, sender = ProductVersion)
def calculate_discounted_price (sender, instance, **kwargs):
    try:
        if instance.discount.percentage:
            discount = float(instance.old_price)*float(instance.discount.percentage)/100
        elif instance.discount.value:
            discount = float(instance.discount.value)
        result = float(instance.old_price)-float(discount)
        instance.new_price = result
    except:
        instance.new_price = instance.old_price


    # if not instance.discount:
    #     result = instance.old_price 
    # else:
    #     if instance.discount.percentage:
    #         discount = float(instance.old_price)*float(instance.discount.percentage)/100
    #     elif instance.discount.value:
    #         discount = float(instance.discount.value)
    #     result = float(instance.old_price)-float(discount)
    # instance.new_price = result


