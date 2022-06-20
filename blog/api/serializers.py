from rest_framework import serializers
from blog.models import BlogCategory, Blog, BlogComment


class BlogCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    blog = serializers.ReadOnlyField(source='blog.title')
    class Meta:
        fields = '__all__'
        model = BlogComment
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class BlogSerializer(serializers.ModelSerializer):
    blog_comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='blog-comments',
    )
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']


class BlogCategorySerializer(serializers.ModelSerializer):
    category_blogs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='blog-detail',
    )
    parent_cat = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = BlogCategory
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']