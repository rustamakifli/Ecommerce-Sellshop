
from django.urls import path
from product.views import product, single_product

urlpatterns = [
    path('product/', product, name='product'),
    path('single_product/<int:id>/', single_product, name='single_product'),
]
