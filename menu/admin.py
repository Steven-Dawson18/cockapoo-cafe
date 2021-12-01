from django.contrib import admin
from .models import Menu, HotDrinks, ColdDrinks


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('name', 'description', 'status', 'created_on')
    search_fields = ['name']


@admin.register(HotDrinks)
class HotDrinksAdmin(admin.ModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('name', 'description', 'price', 'status', 'created_on')
    search_fields = ['name']


@admin.register(ColdDrinks)
class ColdDrinksAdmin(admin.ModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('name', 'description', 'price', 'status', 'created_on')
    search_fields = ['name']
