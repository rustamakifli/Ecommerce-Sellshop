from django.contrib import admin

# Register your models here.

from shop.models import Basket,BasketItems,Order

admin.site.register([Basket ,BasketItems ,Order])