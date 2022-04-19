
from django.urls import path
from product.views import product, single_product,ProductView,ProductListView

urlpatterns = [
    path('product/',  ProductListView.as_view(), name='product'),
    path('single_product/<int:pk>/', ProductView.as_view(), name='single_product'),
]


