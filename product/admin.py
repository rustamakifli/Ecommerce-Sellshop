from django.contrib import admin

# Register your models here.

from product.models import (
    Category, Product, ProductImage, ProductReview, ProductVersion, 
    PropertyName, PropertyValue, Brand
    )
from modeltranslation.admin import TranslationAdmin
from product.models import Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5


@admin.register(Category)
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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'info', )
    list_filter = ('category__title', )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title', 'category','info' ),
            'classes': ('collapse',)
        }),
    ]
 

@admin.register(PropertyName)
class PropertyNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',  )
    list_filter = ('category__title','name' )
    search_fields = ('name', )
    fieldsets = [
        ('Standard info', {
            'fields': ('name', 'category', ),
            'classes': ('collapse',)
        }),
    ]


@admin.register(PropertyValue)
class PropertyValuesAdmin(admin.ModelAdmin):
    list_display = ('name', 'property_name', )
    list_filter = ('property_name', )
    search_fields = ('name', )
    fieldsets = [
        ('Standard info', {
            'fields': ('property_name','name',  ),
            'classes': ('collapse',)
        }),
    ]


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('title','old_price', 'new_price','quantity', 'description', 'is_main' )
    list_filter = ('title','old_price','new_price' )
    search_fields = ('name', )
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('image', 'product_version','is_main' )
    list_filter = ('product_version',)
    search_fields = ('product_version','image' )
    fieldsets = [
        ('Standard info', {
            'fields': ('product_version','image', 'is_main' ),
            'classes': ('collapse',)
        }),
    ]


@admin.register(ProductReview)
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'review')
    list_filter = ('name', 'email',)
    search_fields = ('name', 'email', )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', )
    list_filter = ('title','product',)
    search_fields = ('title', 'product',)
    fieldsets = [
        ('Standard info', {
            'fields': ('title', 'product', ),
            'classes': ('collapse',)
        }),
    ]




