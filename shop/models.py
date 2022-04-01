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
    user = models.ForeignKey(User, related_name='basket_user', on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'

    def __str__(self):
        return self.user


class Order(AbsrtactModel):
    basket = models.ForeignKey(Basket, related_name='basketid', on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User, related_name='basket_order', on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.user
    

class BasketItems(AbsrtactModel):
    price = models.DecimalField(max_digits=12, decimal_places=6)
    count = models.IntegerField()
    subtotal = models.IntegerField()
    product_version = models.ForeignKey(ProductVersion, related_name='product_version_basket_items', on_delete=models.CASCADE, default=1)
    basket = models.ForeignKey(Basket, related_name='basket_basket_items', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Basket item'
        verbose_name_plural = 'Basket items'

    def __str__(self):
        return self.basket