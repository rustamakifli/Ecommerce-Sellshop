from django.contrib import admin
from user.models import BillingAddress
# Register your models here.

@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','reference', 'created_at')
    list_filter = ( 'created_at', )
    search_fields = ('first_name', )
    fieldsets = [
        ('Standard info', {
            'fields': ('first_name', 'last_name','email','country','town','address','mobile_phone','information','reference', ),
            'classes': ('collapse',)
        }),
        # ('Other', {
        #     'fields': ('tags', )
        # }),
    ]