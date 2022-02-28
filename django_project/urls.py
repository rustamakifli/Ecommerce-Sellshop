"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from product.views import product
from user.views import login, account, contact
from blog.views import single_blog, blog
from shop.views import checkout
from cards.views import wish, cart
from product.views import product, single_product
from core.views import about, error404, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('account/', account, name='account'),
    path('single_blog/', single_blog, name='single-blog'),
    path('product/', product, name='product'),
    path('single_product/', single_product, name='single_product'),
    path('wishlist/', wish, name='wishlist'),
    path('blog/', blog, name='blog'),
    path('cart/', cart, name='cart'),
    path('about/', about, name='about'),
    path('error404/', error404, name='error404'),
    path('index/', index, name='index'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    
]
