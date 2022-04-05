from django.db import models

# Create your models here.
class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(AbsrtactModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=40)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class Subscribe(AbsrtactModel):
    email = models.EmailField(max_length=40)

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'

    def __str__(self):
        return self.email