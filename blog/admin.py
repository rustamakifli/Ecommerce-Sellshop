from re import search
from django.contrib import admin

from blog.models import Blog, BlogCategory, BlogComment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at',)
    list_filter = ('category__title', 'created_at', )
    search_fields = ('title', )

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_cat', )
    search_fields = ('title','parent_cat',)

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_filter = ( 'user','created_at', )
    search_fields = ('blog',)

