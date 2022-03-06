from django.db import models

class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Basket(AbsrtactModel):
    # user_id = models.ForeignKey(User, related_name='basket', on_delete=models.CASCADE)
    pass


class Order(AbsrtactModel):
    # basket_id = models.ForeignKey(Basket, related_name='basketid', on_delete=models.CASCADE)
    pass


class BasketItems(AbsrtactModel):
    price = models.DecimalField(max_digits=12, decimal_places=6)
    count = models.IntegerField()
    subtotal = models.IntegerField()
    # product_version_id = models.ForeignKey(ProductVersion, related_name='productversion', on_delete=models.CASCADE)
    # basket_id = models.ForeignKey(Basket, related_name='basket_id', on_delete=models.CASCADE)
