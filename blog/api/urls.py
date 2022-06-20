from django.urls import path
from blog.api import views as api_views

urlpatterns = [
   # bu endpointler sadece click etdikde template-e catmaq ucun yaradilmisdir.
   path('blogpage',api_views.blogpage, name="blogpage"),  
   path('singleblogpage',api_views.singleblogpage, name="singleblogpage"),  

   # blog
   path('blogs/', api_views.BlogListCreateAPIView.as_view(), name='blog-list' ),
   path('blogs/<int:pk>', api_views.BlogDetailAPIView.as_view(), name='blog-detail'),
   path('blogs/<int:blog_pk>/comments', api_views.BlogCommentListCreateAPIView.as_view(), name='blog-comment'),
   # blog category
   path('blog-categories/', api_views.BlogCategoryListCreateAPIView.as_view(), name='blog-categories'),
   path('blog-categories/<int:pk>', api_views.BlogCategoryRetrieveUpdateDestroyAPIView.as_view(), name='blog-categories-detail'),
   # blog comments
   path('blog-comments/<int:pk>', api_views.BlogCommentDetailAPIView.as_view(), name='blog-comments'),
]