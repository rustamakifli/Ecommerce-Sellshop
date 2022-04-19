
from django.urls import path
from product.views import ProductListView, single_product

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product'),
    path('single_product/<int:id>/', single_product, name='single_product'),
]
