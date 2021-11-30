from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Menu, HotDrinks


class MenuList(generic.ListView):
    model = Menu
    queryset = Menu.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/menu.html'
    paginate_by = 6


class HotDrinksList(generic.ListView):
    model = HotDrinks
    queryset = HotDrinks.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/hot-drinks.html'
