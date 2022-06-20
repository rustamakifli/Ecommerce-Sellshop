from django.urls import path
from product.api import views as api_views

urlpatterns = [
    path('products/', api_views.ProductListCreateApi.as_view(), name="product_list"),
    path('products/<int:pk>', api_views.ProductDetailApi.as_view(), name="product-detail"),
    path('product-versions/', api_views.ProductVersionListCreateApi.as_view(), name="product-version-list"),
    path('categories/', api_views.CategoryListCreateApi.as_view(), name="category-list"),
]
