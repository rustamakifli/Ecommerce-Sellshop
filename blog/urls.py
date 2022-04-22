
from django.urls import path
from blog.views import SingleBlogDetailView, BlogListView

urlpatterns = [
    path('single_blog/<int:pk>/', SingleBlogDetailView.as_view(), name='single-blog'),
    path('blog/', BlogListView.as_view(), name='blog'),
]
