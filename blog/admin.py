from re import search
from django.contrib import admin

# Register your models here.

from blog.models import Blog, BlogReviews, BlogCategory, BlogComment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image','description', 'created_at')
    list_filter = ('category__title', 'created_at', )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title', 'category', ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title',),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ( 'comment', 'user','created_at')
    list_filter = ( 'comment','user','created_at', )
    search_fields = ('comment', )
    # fieldsets = [
    #     ('Standard info', {
    #         'fields': ('user', ),
    #         'classes': ('collapse',)
    #     }),
    #     # ('Other', {
    #     #     'fields': ('tags', )
    #     # }),
    # ]


admin.site.register([ BlogReviews,])
