'''Review Admin'''
from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Filters, displays and search for django admin"""
    list_filter = ('status', 'created_on', 'author')
    list_display = ('title', 'author', 'body', 'status', 'created_on',
                    'approved')
    search_fields = ['author']
