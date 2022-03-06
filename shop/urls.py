
from django.urls import path
from shop.views import checkout, order

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('order/', order, name='order'),
]
