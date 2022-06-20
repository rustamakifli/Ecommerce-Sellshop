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


class Order(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE, default="")
	ordered_at = models.DateTimeField(verbose_name="Ordered at", null=True, blank=True)
	complete = models.BooleanField(verbose_name="Completed?",default=False)
	transaction_id = models.CharField(max_length=100, null=True)
	product = models.ManyToManyField(ProductVersion,blank=True)
	# shipping_address = models.OneToOneField(
    #     ShippingAddress, null=True, blank=True, verbose_name="Shipping Address", on_delete=models.CASCADE)
	


	def __str__(self) -> str:
		  return f"{self.customer}"
	  
class OrderItem(models.Model):
    product = models.ForeignKey(ProductVersion, on_delete=models.SET_NULL, null=True, blank=True, related_name="Product_Order")
    order = models.ForeignKey(Order, on_delete=models.CASCADE,blank=True,null=True, related_name="User_Order")
    quantity = models.PositiveIntegerField(verbose_name="Quantity", default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(verbose_name="Price", default=0.00)
    

    def __str__(self) -> str:
		    return f"{self.order}"
   

class Basket(AbstrasctModel):
    user = models.ForeignKey(User, related_name='baskets', on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'

    def __str__(self):
        return self.user


# class Order(AbsrtactModel):
#     basket = models.ForeignKey(Basket, related_name='orders', on_delete=models.CASCADE,default=1)
#     user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE,default=1)

#     class Meta:
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'

#     def __str__(self):
#         return self.user
    

class BasketItem(AbstrasctModel):
    product_version = models.ForeignKey(ProductVersion, related_name='basket_items', on_delete=models.CASCADE, default=1)
    basket = models.ForeignKey(Basket, related_name='basket_items', on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=12, decimal_places=6)
    count = models.IntegerField()
    subtotal = models.IntegerField()

    class Meta:
        verbose_name = 'Basket item'
        verbose_name_plural = 'Basket items'

    def __str__(self):
        return self.basket