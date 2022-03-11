from django.db import models

class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Wishlist(AbsrtactModel):
    # user = models.ForeignKey(User, related_name='blogreviews', on_delete=models.CASCADE)
    # product_version_id = models.ForeignKey(ProductVersion, related_name='wishlist', on_delete=models.CASCADE)
    pass