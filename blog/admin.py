from django.contrib import admin

# Register your models here.

from blog.models import Blog, BlogReviews, BlogCategory, BlogComment

admin.site.register([Blog, BlogReviews, BlogCategory, BlogComment])
