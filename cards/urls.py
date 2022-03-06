
from django.urls import path
from cards.views import cart, wish

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('wishlist/', wish, name='wishlist'),
]
