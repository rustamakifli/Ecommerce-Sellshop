from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from product.models import ProductVersion
from sellshop.utils.abstract_models import AbstrasctModel

User = get_user_model()



class Wishlist(AbstrasctModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="",related_name="wishlistofUser")
    product = models.ManyToManyField(ProductVersion, blank=True, related_name='Product_wishlist')

    def __str__(self):
        return f"{self.user}"


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
