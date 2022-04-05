from django.contrib import admin
from core.models import Contact, Subscribe

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('name', 'email', )
    search_fields = ('name', 'email', )


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    list_filter = ('email', )
    search_fields = ('email', )