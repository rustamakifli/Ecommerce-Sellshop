from rest_framework import generics
from rest_framework.generics import get_object_or_404

from product.api.serializers import (
    CategorySerializer, ProductSerializer, ProductVersionSerializer,
    PropertyNameSerializer, PropertyValueSerializer, ProductImageSerializer,
    ProductReviewSerializer, BrandSerializer,)

from product.models import (
    Category, Product, ProductVersion, PropertyName,
    PropertyValue, ProductImage, ProductReview, Brand,
    )


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


class PropertyValueListCreateAPIView(generics.ListCreateAPIView):
    queryset = PropertyValue.objects.all()
    serializer_class = PropertyValueSerializer


class PropertyValueDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyValue.objects.all()
    serializer_class = PropertyValueSerializer


class PropertyNameListCreateAPIView(generics.ListCreateAPIView):
    queryset = PropertyName.objects.all()
    serializer_class = PropertyNameSerializer


class PropertyNameDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyName.objects.all()
    serializer_class = PropertyNameSerializer


class ProductVersionListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer


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