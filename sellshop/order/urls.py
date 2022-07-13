
from django.urls import path
from order.views import cart, wish,order,CheckoutShipping

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('wishlist/', wish, name='wishlist'),
    path('checkout/', CheckoutShipping.as_view(), name='checkout'),
    path('order/', order, name='order'),

]
