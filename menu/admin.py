from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('name', 'description', 'price', 'status', 'created_on')
    search_fields = ['name']
