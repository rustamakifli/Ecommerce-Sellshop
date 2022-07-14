from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from csv import *
from nested_admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline

from product.models import (Category, Brand, Discount, Product, Tag, Color, Size, ProductVersion, ProductImage, ProductReview)
myModels = [Category, Brand, Tag, Color, Size, ProductReview, Discount,]
admin.site.register(myModels)


class ProductImageInline(NestedTabularInline):
    model = ProductImage
    extra = 5
    classes = ['collapse']


class ProductVersionInline(NestedStackedInline):
    model = ProductVersion
    extra = 1
    inlines = [ProductImageInline,]
    classes = ['collapse']




class ProductAdmin(NestedModelAdmin):
    inlines = [ProductVersionInline,]
    list_filter = ('title', 'category', 'brand', 'description', 'tags', 'featured')
    fieldsets = (
        ('Main', {
            'fields': ('title', 'category', 'brand', 'description'),
            'classes': ('order-0', 'baton-tabs-init', 'baton-tab-inline-attribute', 'baton-tab-group-fs-tech--inline-feature', ),

        }),
        ('Additional', {
            'fields': ('tags', 'featured'),
            'classes': ('tab-fs-tech', ),

        }),
    )

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(TranslationAdmin):
    list_display = ('title', 'parent_cat',)
    list_filter = ('title',)
    search_fields = ('title', )
    classes = ['collapse']
    

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
    ordering = ('-confirm',)


class BrandAdmin(TranslationAdmin):
    list_display = ('title',)


class DiscountAdmin(TranslationAdmin):
    list_display = ('title',)


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
