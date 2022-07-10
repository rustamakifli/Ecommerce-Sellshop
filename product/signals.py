from django.db.models.signals import pre_save
from product.models import ProductVersion, ProductImage
from django.dispatch import receiver

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


@receiver(pre_save, sender = ProductVersion)
def title_inherit_product_title (sender, instance, **kwargs):
    try:
        if not instance.quantity:          
            instance.title = f'{instance.product.brand} {instance.product.title} {instance.color} (Out of Stock)'
        else:
            instance.title = f'{instance.product.brand} {instance.product.title} {instance.color}'
    except:
        instance.title = " "


    # if not instance.discount:
    #     result = instance.old_price 
    # else:
    #     if instance.discount.percentage:
    #         discount = float(instance.old_price)*float(instance.discount.percentage)/100
    #     elif instance.discount.value:
    #         discount = float(instance.discount.value)
    #     result = float(instance.old_price)-float(discount)
    # instance.new_price = result


# @receiver(pre_save, sender = ProductVersion)
# def copy_images (sender, instance, **kwargs):
#     if not instance.product_images:
#         instance.product_images = ProductImage.objects.all().first()
#         instance.save()