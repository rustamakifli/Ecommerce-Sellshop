from dataclasses import fields
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from csv import *

from product.models import (Category, Brand, Product, Tag, Color, Size, ProductVersion, ProductImage, ProductReview)
myModels = [Category, Brand, Tag, Color, Size, ProductReview]
admin.site.register(myModels)
from nested_admin import NestedModelAdmin, NestedTabularInline


class ProductImageInline(NestedTabularInline):
    model = ProductImage
    extra = 5


class ProductVersionInline(NestedTabularInline):
    model = ProductVersion
    extra = 0
    inlines = [ProductImageInline,]

    list_filter = ('color', 'size' )
    exclude = ('title',)


class ProductAdmin(NestedModelAdmin):
    inlines = [ProductVersionInline,]

    # list_display = ('title', 'category', 'brand', 'description',)
    # list_filter = ('category__title', )
    # search_fields = ('title', )
    # fieldsets = [
    #     ('Standard info', {
    #         'fields': ('title', 'category','info' ),
    #         'classes': ('collapse',)
    #     }),
    # ]



admin.site.register(Product, ProductAdmin)


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
