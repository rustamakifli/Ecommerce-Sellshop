from rest_framework import serializers
from blog.models import BlogCategory, Blog, BlogReview, BlogComment
from user.models import User



class BlogReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogReview
        exclude = ['blog']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BlogCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = BlogComment
        exclude = ['blog']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class BlogSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']


class BlogCategorySerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = BlogCategory
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


# bu serializer test meqsedlidir. silinecek.
class AuthorSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'bio', 'sex', 'phone_number', 'birthdate', 'groups', 'user_permissions' ]
        read_only_fields = ['id', 'username', 'first_name', 'last_name', 'email', 'image']