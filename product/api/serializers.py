from rest_framework import serializers
from product.models import (
    Category, Product, ProductVersion, PropertyName, PropertyValue, ProductImage, ProductReview, Brand
    )


class ProductVersionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product = serializers.ReadOnlyField(source='product.title')
    class Meta:
        fields = '__all__'
        model = ProductVersion
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    product_versions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-version-list',
    )
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    category_products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail',
    )
    parent_cat = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']















