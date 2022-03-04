from django.contrib import admin

# Register your models here.

from blog.models import Blog, BlogReviews

admin.site.register([Blog, BlogReviews])