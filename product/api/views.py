from rest_framework import generics
from rest_framework.generics import get_object_or_404


from product.api.serializers import ProductVersionSerializer, ProductSerializer, CategorySerializer
from product.models import (
    Category, Product, ProductVersion, PropertyName, PropertyValue, ProductImage, ProductReview, Brand
    )

class ProductVersionListCreateApi(generics.ListCreateAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer


class ProductListCreateApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListCreateApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
