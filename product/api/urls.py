from django.urls import path
from product.api import views as api_views


urlpatterns = [
    # bu endpointler sadece click etdikde template-e catmaq ucun yaradilmisdir.
    path('product/',api_views.product, name='product'),
    path('single_product/', api_views.single_product, name='single_product'),

    path('categories/', api_views.CategoryListCreateAPIView.as_view(), name="category-list"),
    path('categories/<int:pk>', api_views.CategoryDetailAPIView.as_view(), name="category-detail"),

    path('products/', api_views.ProductListCreateAPIView.as_view(), name="product_list"),
    path('products/<int:pk>', api_views.ProductDetailAPIView.as_view(), name="product-detail"),

    path('product-versions/', api_views.ProductVersionListCreateAPIView.as_view(), name="product-version-list"),
    path('product-versions/<int:pk>', api_views.ProductVersionDetailAPIView.as_view(), name="product-version-detail"),
    path('product-versions/<int:product_version_pk>/images', api_views.ProductImageListCreateAPIView.as_view(), name='product-version-images'),
    path('product-versions/<int:product_version_pk>/reviews', api_views.ProductReviewListCreateAPIView.as_view(), name='product-version-images'),

    path('property-names/', api_views.PropertyNameListCreateAPIView.as_view(), name="property-name-list"),
    path('property-names/<int:pk>', api_views.PropertyNameDetailAPIView.as_view(), name="property-name-detail"),

    path('property-values/', api_views.PropertyValueListCreateAPIView.as_view(), name="property-value-list"),
    path('property-values/<int:pk>', api_views.PropertyValueDetailAPIView.as_view(), name="property-value-detail"),

    path('product-images/<int:pk>', api_views.ProductImageDetailAPIView.as_view(), name="product-image-detail"),

    path('product-reviews/', api_views.ProductReviewListCreateAPIView.as_view(), name="product-review-list"),
    path('product-reviews/<int:pk>', api_views.ProductReviewDetailAPIView.as_view(), name="product-review-detail"),

    path('brands/', api_views.BrandListCreateAPIView.as_view(), name="brand-list"),
    path('brands/<int:pk>', api_views.BrandDetailAPIView.as_view(), name="brand-detail"),
]
