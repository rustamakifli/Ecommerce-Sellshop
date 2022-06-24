from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from product.api.serializers import (
    CategorySerializer, ProductSerializer, ProductVersionSerializer,
    TagSerializer, ColorSerializer, SizeSerializer, ProductImageSerializer,
    ProductReviewSerializer, BrandSerializer,)

from product.models import (Category, Brand, Product, Tag, Color, Size, ProductVersion, ProductImage, ProductReview)


class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ColorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class ProductReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class ProductImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    # path('product-versions/<int:product_version_pk>/images', api_views.ProductImageListCreateAPIView.as_view(), name='product-version-images'),
    def perform_create(self, serializer):
        product_version_pk = self.kwargs.get('product_version_pk')
        product_version = get_object_or_404(ProductVersion, pk=product_version_pk)
        serializer.save(product_version=product_version)

    def get_queryset(self):
        product_version = self.kwargs.get('product_version_pk')
        return super().get_queryset().filter(product_version=product_version)


class ProductImageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductVersionListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer

    # get filtered data
    # http://127.0.0.1:8000/api/product-versions/?tags={}
    def get(self, request, *args, **kwargs):
        queryset = ProductVersion.objects.filter(quantity__gt=0)
        featured = request.GET.get('featured')
        is_main = request.GET.get('is_main')
        product = request.GET.get('product') 
        tags = request.GET.get('tags')
        if product:
            queryset = queryset.filter(product__id=product) 
        if tags:
            queryset = queryset.filter(tags__id=tags) 
        if featured:
            queryset = queryset.filter(featured=featured)
        if is_main:
            queryset = queryset.filter(is_main=is_main)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductVersionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


