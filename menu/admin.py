
""" Menu admin.py"""
from django.contrib import admin
from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Filters, displays and search for django admin"""
    list_filter = ('name', )
    list_display = ('name', 'description')
    search_fields = ['name']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Filters, displays and search for django admin"""
    list_filter = ('name', 'category')
    list_display = ('name', 'category', 'description', 'price', 'status',
                    'created_on')
    search_fields = ['name']
