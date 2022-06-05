
from django.urls import path
from product.api.views import ProductListAPI

urlpatterns = [
    path('product/', ProductListAPI.as_view(), )
]
