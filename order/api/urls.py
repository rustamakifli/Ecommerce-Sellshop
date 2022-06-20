from . import views
from django.urls import path, include

urlpatterns = [
    path('cart/', views.OrderView.as_view(), name='card'),
    path('cart-item/', views.OrderItemView.as_view(), name='cart_item'),
]