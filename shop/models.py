from django.db import models
from django.contrib.auth import get_user_model
from product.models import ProductVersion

User = get_user_model()

class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Basket(AbsrtactModel):
    user = models.ForeignKey(User, related_name='basket', on_delete=models.CASCADE,default=1)


class Order(AbsrtactModel):
    basket = models.ForeignKey(Basket, related_name='basketid', on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User, related_name='basket', on_delete=models.CASCADE,default=1)
    


class Order(AbsrtactModel):
    basket = models.ForeignKey(Basket, related_name='basketid', on_delete=models.CASCADE,default=1)


class BasketItems(AbsrtactModel):
    price = models.DecimalField(max_digits=12, decimal_places=6)
    count = models.IntegerField()
    subtotal = models.IntegerField()
    product_version = models.ForeignKey(ProductVersion, related_name='productversion', on_delete=models.CASCADE, default=1)
    basket = models.ForeignKey(Basket, related_name='basket_id', on_delete=models.CASCADE,default=1)
