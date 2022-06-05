from dataclasses import field
from itertools import product
from rest_framework import serializers
from product.models import Category, Product, ProductVersion


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "title",
        ]


# class CategorieTreeSerializer(CategorySerializer):
#     childs = serializers.SerializerMethodField()

#     class Meta(CategorySerializer.Meta):
#         fields = (
#             "title"
#         )

#     def get_childs(self, obj):
#         pass


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = [
            "category",
            "title",
            "info",
        ]


class ProductVersionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ProductVersion
        fields = [
            "product",
            "title",
            "old_price",
            "new_price",
            "quantity",
            "description",
        ]

