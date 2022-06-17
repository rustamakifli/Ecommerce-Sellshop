from django.urls import path
from blog.api import views as api_views

urlpatterns = [
   path('blogs/', api_views.BlogListCreateAPIView.as_view(), name='blog-list' ),
   path('blogs/<int:pk>', api_views.BlogDetailAPIView.as_view(), name='blog-detail'),
   path('blogs/<int:blog_pk>/create-comment', api_views.BlogCommentListCreateAPIView.as_view(), name='blog-create-comment'),

   path('blog-comments/<int:pk>', api_views.BlogCommentDetailAPIView.as_view(), name='blog-comments'),
   
   path('blog-categories/', api_views.BlogCategoryListCreateAPIView.as_view(), name='blog-categories'),
   path('blog-categories/<int:pk>', api_views.BlogCategoryRetrieveUpdateDestroyAPIView.as_view(), name='blog-categories-detail'),

   # bu endpointler test meqsedi ile yazilmisdir. Daha sonra silinecek. Ehtiyac yoxdur.
   path('blog-comments/', api_views.BlogCommentListCreateAPIView.as_view(), name='blog-comments'),
]