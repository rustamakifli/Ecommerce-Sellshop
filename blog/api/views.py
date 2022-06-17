from rest_framework import generics
from rest_framework.generics import get_object_or_404
from user.models import User


from blog.api.serializers import BlogSerializer, BlogCommentSerializer, BlogCategorySerializer, BlogReviewSerializer, AuthorSerializer
from blog.models import BlogCategory, Blog, BlogReview, BlogComment


class AuthorListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class BlogCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all().order_by('id')
    serializer_class = BlogCategorySerializer


class BlogCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

    def perform_create(self, serializer):
        # path('blogs/<int:blog_pk>/create-comment', api_views.YorumCreateAPIView.as_view(), name='blog-create-comment'),
        blog_pk = self.kwargs.get('blog_pk')
        blog = get_object_or_404(Blog, pk=blog_pk)
        print(blog)
        serializer.save(blog=blog)


class BlogCommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer  
