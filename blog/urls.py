
from django.urls import path
from blog.views import blog, SingleBlogDetailView

urlpatterns = [
    path('single_blog/<int:pk>/', SingleBlogDetailView.as_view(), name='single-blog'),
    path('blog/', blog, name='blog'),
]
