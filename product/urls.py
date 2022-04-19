
from django.urls import path
from product.views import product, single_product,ProductView

urlpatterns = [
    path('product/', product, name='product'),
    path('single_product/<int:pk>/', ProductView.as_view(), name='single_product'),
]
