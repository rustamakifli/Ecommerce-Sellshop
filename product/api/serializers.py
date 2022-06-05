from unicodedata import category
from rest_framework import serializers
from product.models import ProductVersion,Product,Category,ProductImages,PropertyName,PropertyValues
from collections import OrderedDict


class PropertyValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyValues
        fields = (
            'name',

        )


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = (
            'id',
            'parent_cat',
            'title',
        )

    def to_representation(self, instance):
        result = super(CategorySerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class ProductSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id', 
            'category',
            'title',
            'info',
        )

class ProductImageSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProductImages
        fields = (
            'image',
            
        )

class ProductReadSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    product_image = ProductImageSerializer()
    property = PropertyValueSerializer()
    
    class Meta:
        model = ProductVersion
        fields = (
            
            'product',
            'product_image',
            'title',
            'property',
            'old_price',    
            'new_price',
            'quantity',
            'description',
        )


    def to_representation(self, instance):
        result = super(ProductReadSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])

   
class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVersion
        fields = (
            'product',
            'title',
            'old_price',    
            'new_price',
            'quantity',
            'description',
        )
