import imp
from django.urls import path
from product.api.views import ProductListCreateApi,ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('product/', ProductListCreateApi.as_view(),),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),)
]
