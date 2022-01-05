from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Menu, HotDrinks, ColdDrinks, Sandwich, Cake


class MenuListView(ListView):
    model = Menu
    queryset = Menu.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/menu.html'


# class HotDrinksList(generic.ListView):
#     model = HotDrinks
#     queryset = HotDrinks.objects.filter(status=1).order_by('-created_on')
#     template_name = 'menu/hot-drinks.html'


class ColdDrinksList(generic.ListView):
    model = ColdDrinks
    queryset = ColdDrinks.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/cold-drinks.html'


class SandwichList(generic.ListView):
    model = Sandwich
    queryset = Sandwich.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/snacks.html'


class CakeList(generic.ListView):
    model = Cake
    queryset = Cake.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/cakes.html'


class HotDrinksListView(ListView):
    model = HotDrinks
    queryset = HotDrinks.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/hot-drinks.html'


class HotdrinksCreateView(LoginRequiredMixin, CreateView):
    model = HotDrinks
    fields = ['name', 'description', 'image', 'price']
    template_name = 'menu/create_hotdrink.html'
    success_message = "Drink created"
    success_url = reverse_lazy('hot-drinks')


class HotdrinksUpdateView(LoginRequiredMixin, UpdateView):
    model = HotDrinks
    fields = ['name', 'description', 'image', 'price']
    template_name = 'menu/update_hotdrink.html'
    success_message = "Drink has been updated"
    success_url = reverse_lazy('hot-drinks')


class HotdrinksDeleteView(LoginRequiredMixin, DeleteView):
    model = HotDrinks
    template_name = 'menu/delete-hot-drink.html'
    success_message = "Drink has been deleted"
    success_url = reverse_lazy('hot-drinks')
