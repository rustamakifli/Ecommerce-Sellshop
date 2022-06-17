
from rest_framework import serializers
from blog.models import BlogCategory, Blog, BlogReview, BlogComment


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogReview
        exclude = ['blog']


class BlogCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = BlogComment
        exclude = ['blog']


class BlogSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
