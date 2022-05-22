from re import search
from django.contrib import admin

# Register your models here.

from blog.models import Blog, BlogReview, BlogCategory, BlogComment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author','description', 'created_at')
    list_filter = ('category__title', 'created_at', )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title', 'category','author','image','description','content', ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_cat' )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title','parent_cat',),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email','created_at')
    list_filter = ( 'name','created_at', )
    search_fields = ('comment','name' )
    fieldsets = [
        ('Standard info', {
            'fields': ('blog','name', 'email','comment'),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]


admin.site.register([ BlogReview,])
