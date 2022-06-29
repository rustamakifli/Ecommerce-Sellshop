from django.urls import path
from . import views as template_views


urlpatterns = [
   # bu endpointler sadece click etdikde template-e catmaq ucun yaradilmisdir.
   path('blogpage',template_views.blogpage, name="blogpage"),  
   path('blogpage/<int:id>/',template_views.singleblogpage, name="singleblogpage"),  
]





# urlpatterns = [
#     path('single_blog/<slug:slug>/', SingleBlogDetailView.as_view(), name='single-blog'),
#     path('blog/', BlogListView.as_view(), name='blog'),
# ]
