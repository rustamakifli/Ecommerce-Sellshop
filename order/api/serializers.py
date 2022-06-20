import random
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers

from order.models import Order, OrderItem
from product.api.serializers import ProductReadSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("id", "customer", "product","complete")

    def get_products(self, obj):
        qs = obj.product.all()
        return ProductReadSerializer(qs, many=True).data

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer() 
    is_ordered = serializers.SerializerMethodField()
    coupon_discount = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ("product", "quantity", "price", "date_added","order")

    def get_is_ordered(self, obj):
        qs = obj.cart.is_ordered
        return qs

    # def get_coupon_discount(self, obj):
    #     if obj.cart.coupon:
    #         qs = obj.cart.coupon.discount
    #         return qs
    #     return 0