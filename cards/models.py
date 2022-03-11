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
<<<<<<< HEAD
    # user = models.ForeignKey(User, related_name='blogreviews', on_delete=models.CASCADE)
    # product_version_id = models.ForeignKey(ProductVersion, related_name='wishlist', on_delete=models.CASCADE)
    pass
=======
    user = models.ForeignKey(User, related_name='blogreviews', on_delete=models.CASCADE)
    product_version = models.ForeignKey(ProductVersion, related_name='wishlist', on_delete=models.CASCADE)
>>>>>>> rustamakifli
