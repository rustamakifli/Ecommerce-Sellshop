from django.contrib import admin

# Register your models here.

from shop.models import Basket,BasketItems,Order

@admin.register(BasketItems)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('basket', 'price', 'count','product_version', )
    list_filter = ('basket','product_version',)
    search_fields = ('product_version', )
    fieldsets = [
        ('Standard info', {
            'fields': ('basket',  ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

admin.site.register([Basket  ,Order])
