
from django.urls import path
from blog.views import single_blog,BlogListView

urlpatterns = [
    path('single_blog/', single_blog, name='single-blog'),
    path('blog/', BlogListView.as_view(), name='blog'),
]
