from django.contrib import admin

# Register your models here.

from product.models import Category, Product, ProductImages, ProductReviews, ProductVersion, PropertyName, PropertyValues, Brand


class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_cat' )
    list_filter = ('title', )
    search_fields = ('title', )
    fieldsets = [
        ('Standard info', {
            'fields': ('title',  'parent_cat'),
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
            'fields': ('title', 'category','info' ),
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
            'fields': ('property_name','name',  ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('title','old_price', 'new_price','quantity', 'description', 'is_main' )
    list_filter = ('title','old_price','new_price' )
    search_fields = ('name', )
    inlines = [ProductImageInline]
    # fieldsets = [
    #     ('Standard info', {
    #         'fields': ('title','old_price','new_price','product','description','is_main','quantity', 'property'),
    #         'classes': ('collapse',)
    #     }),
    #     ('Other', {
    #         'fields': ('tags', )
    #     }),
    # ]

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('image', 'product_version','is_main' )
    list_filter = ('product_version',)
    search_fields = ('product_version','image' )
    fieldsets = [
        ('Standard info', {
            'fields': ('product_version','image', 'is_main' ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

@admin.register(ProductReviews)
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
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]

# admin.site.register([Category,])


