
from django.urls import path
from blog.views import single_blog, blog

urlpatterns = [
    path('single_blog/', single_blog, name='single-blog'),
    path('blog/', blog, name='blog'),
]
