from django.contrib import admin

# Register your models here.

from product.models import Category, Product, ProductImages, ProductReviews, ProductVersion, PropertyName, PropertyValues, Brand

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',  )
    list_filter = ('title', )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title',  ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'info', )
    list_filter = ('category__title', )
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
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(PropertyValues)
class PropertyValuesAdmin(admin.ModelAdmin):
    list_display = ('name', 'property_name', )
    list_filter = ('property_name', )
    search_fields = ('name', )
    fieldsets = [
        ('Standard info', {
            'fields': ('name',  ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','quantity', 'description', 'is_main' )
    list_filter = ('title','price' )
    search_fields = ('name', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title','price'  ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('image', 'product_version','is_main' )
    list_filter = ('product_version',)
    search_fields = ('product_version','image' )
    fieldsets = [
        ('Standard info', {
            'fields': ('image',  ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_version','title', 'info' )
    list_filter = ('product_version','user','title')
    search_fields = ('product_version','title' )
    fieldsets = [
        ('Standard info', {
            'fields': ('user',  ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', )
    list_filter = ('title','product',)
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title',  ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

# admin.site.register([Category,])