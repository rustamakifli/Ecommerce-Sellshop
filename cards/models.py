from django.db import models
from django.contrib.auth import get_user_model
from product.models import ProductVersion
User = get_user_model()


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Wishlist(AbstractModel):
    user = models.ForeignKey(User, related_name='wishlists', on_delete=models.CASCADE, default=1)
    product_version = models.ForeignKey(ProductVersion, related_name='wishlists', on_delete=models.CASCADE, default=1)
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    # def __str__(self):
    #     return self.user