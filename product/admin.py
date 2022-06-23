from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from csv import *

from product.models import (Category, Brand, Product, Tag, Color, Size, ProductVersion, ProductImage, ProductReview)
myModels = [Category, Brand, Product, Tag, Color, Size, ProductVersion, ProductImage, ProductReview]
admin.site.register(myModels)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5


class ProductVersionAdmin(TranslationAdmin):
    list_filter = ('title', 'tags', )
    search_fields = ('tags', )
    inlines = [ProductImageInline]


class CategoryAdmin(TranslationAdmin):
    list_display = ('title', 'parent_cat',)
    list_filter = ('title', )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title',  'parent_cat',),
            'classes': ('collapse',)
        }),
    ]


class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'info', 'brand',)
    list_filter = ('category__title', )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title', 'category','info' ),
            'classes': ('collapse',)
        }),
    ]


class ProductImagesAdmin(TranslationAdmin):
    list_display = ('image', 'product_version','is_main' )
    list_filter = ('product_version',)
    search_fields = ('product_version','image' )
    fieldsets = [
        ('Standard info', {
            'fields': ('product_version','image', 'is_main' ),
            'classes': ('collapse',)
        }),
    ]


class ProductReviewsAdmin(TranslationAdmin):
    list_filter = ('user', 'rating',)
    search_fields = ('review', 'user', 'rating',)
    readonly_fields = ["user",]


class BrandAdmin(TranslationAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    fieldsets = [
        ('Standard info', {
            'fields': ('title',),
            'classes': ('collapse',)
        }),
    ]


class TagAdmin(TranslationAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title',)


class ColorAdmin(TranslationAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title',)


class SizeAdmin(TranslationAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title',)
