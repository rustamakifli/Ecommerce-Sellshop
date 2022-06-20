from django.contrib import admin

# Register your models here.
from order.models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'ordered_at','complete' ,'transaction_id')
    list_filter = ('ordered_at', )
    search_fields = ('customer', )
    fieldsets = [
        ('Standard info', {
            'fields': ('customer', 'complete' ,'transaction_id' ),
            'classes': ('collapse',)
        }),
    ]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order','quantity' ,'date_added','price')
    list_filter = ('order', )
    search_fields = ('product', )
    fieldsets = [
        ('Standard info', {
            'fields': ('product',  'order','quantity' , ),
            'classes': ('collapse',)
        }),
    ]


@admin.register(BasketItem)
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

admin.site.register([Basket ])

admin.site.register([Wishlist])
