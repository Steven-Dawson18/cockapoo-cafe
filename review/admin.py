from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('title', 'author', 'body', 'status', 'created_on')
    search_fields = ['author']
