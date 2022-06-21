from itertools import product
from rest_framework import serializers
from product.models import (
    Category, Product, ProductVersion, PropertyName, PropertyValue, ProductImage, ProductReview, Brand
    )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    # product_version = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProductImage
        fields = '__all__'


class PropertyValueSerializer(serializers.ModelSerializer):
    property_name = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = PropertyValue
        fields = '__all__'


class PropertyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyName
        fields = '__all__'


class ProductVersionSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(read_only=True,)
    # serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='blog-version-detail',
    # )
    user = serializers.StringRelatedField(read_only=True)
    # product = serializers.ReadOnlyField(source='product.title')
    # property_values =PropertyValueSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = ProductVersion
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    product_versions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-version-detail',
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
        read_only_fields = ['id', 'title_en','title_az', 'created_at', 'updated_at']















