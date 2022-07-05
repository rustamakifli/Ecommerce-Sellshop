from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from product.models import ProductVersion
from sellshop.utils.abstract_models import AbstrasctModel
User = get_user_model()


# class AbstractModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


class Wishlist(AbstrasctModel):
    user = models.ForeignKey(User, related_name='wishlists', on_delete=models.CASCADE, default=1)
    product_version = models.ForeignKey(ProductVersion, related_name='wishlists', on_delete=models.CASCADE, default=1)
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    # def __str__(self):
    #     return self.user

class Order(AbstrasctModel):
    basket = models.OneToOneField('Basket', default='', on_delete=models.CASCADE)

    total = models.DecimalField('Total', decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.total)


class Basket(AbstrasctModel):
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  ##### status = is_ordered

    sub_total = models.DecimalField('Sub Total', decimal_places=2, max_digits=10,)

    def __str__(self):
        return str(self.status)


class BasketItem(AbstrasctModel):
    basket = models.ForeignKey(Basket, default='', related_name='basketitems', on_delete=models.CASCADE)
    productVersion = models.ForeignKey(ProductVersion, related_name='Product_Cart',default='', on_delete=models.CASCADE, verbose_name='Product Version')

    price = models.DecimalField('Price', decimal_places=2, max_digits=10)
    sub_total = models.DecimalField('Sub-Total', decimal_places=2, max_digits=10)
    count = models.IntegerField('Count')

    def __str__(self):
        return str(self.sub_total)



# class Order(AbsrtactModel):
#     basket = models.ForeignKey(Basket, related_name='orders', on_delete=models.CASCADE,default=1)
#     user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE,default=1)

#     class Meta:
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'

#     def __str__(self):
#         return self.user
    

# class BasketItem(AbstrasctModel):
#     product_version = models.ForeignKey(ProductVersion, related_name='basket_items', on_delete=models.CASCADE, default=1)
#     basket = models.ForeignKey(Basket, related_name='basket_items', on_delete=models.CASCADE, default=1)
#     price = models.DecimalField(max_digits=12, decimal_places=6)
#     count = models.IntegerField()
#     subtotal = models.IntegerField()

#     class Meta:
#         verbose_name = 'Basket item'
#         verbose_name_plural = 'Basket items'

#     def __str__(self):
#         return self.basket