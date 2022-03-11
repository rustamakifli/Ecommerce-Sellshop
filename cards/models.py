from django.db import models
from django.contrib.auth import get_user_model
from product.models import ProductVersion
User = get_user_model()


class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Wishlist(AbsrtactModel):
    user = models.ForeignKey(User, related_name='user_wishlist', on_delete=models.CASCADE, default=1)
    product_version = models.ForeignKey(ProductVersion, related_name='product_version_wishlist', on_delete=models.CASCADE, default=1)
