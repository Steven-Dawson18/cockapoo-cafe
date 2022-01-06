from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Menu, HotDrinks, ColdDrinks, Sandwich, Cake
from django.http import HttpResponseRedirect


# menu options
class MenuListView(ListView):
    model = Menu
    queryset = Menu.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/menu.html'


# Hot drinks menu
class HotDrinksListView(ListView):
    model = HotDrinks
    queryset = HotDrinks.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/hot-drinks.html'

    def get_context(self):
        item = get_object_or_404(HotDrinks, id=self.pk)
        total_likes = item.total_likes()
        context["total_likes"] = total_likes
        return context


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


def LikeView(request, pk):
    hotdrink = get_object_or_404(HotDrinks, id=pk)
    hotdrink.likes.add(request.user)
    return HttpResponseRedirect(reverse('hot-drinks'))


# Cold drinks menu
class ColdDrinksListView(ListView):
    model = ColdDrinks
    queryset = ColdDrinks.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/cold-drinks.html'


class ColdDrinksCreateView(LoginRequiredMixin, CreateView):
    model = ColdDrinks
    fields = ['name', 'description', 'image', 'price']
    template_name = 'menu/create_colddrink.html'
    success_message = "Drink created"
    success_url = reverse_lazy('cold-drinks')


class ColdDrinksUpdateView(LoginRequiredMixin, UpdateView):
    model = ColdDrinks
    fields = ['name', 'description', 'image', 'price']
    template_name = 'menu/update_colddrink.html'
    success_message = "Drink has been updated"
    success_url = reverse_lazy('cold-drinks')


class ColdDrinksDeleteView(LoginRequiredMixin, DeleteView):
    model = ColdDrinks
    template_name = 'menu/delete-cold-drink.html'
    success_message = "Drink has been deleted"
    success_url = reverse_lazy('cold-drinks')


# Sandwich menu
class SandwichesListView(ListView):
    model = Sandwich
    queryset = Sandwich.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/sandwich.html'


class SandwichesCreateView(LoginRequiredMixin, CreateView):
    model = Sandwich
    fields = ['name', 'description', 'image', 'price']
    template_name = 'menu/create_sandwich.html'
    success_message = "sandwich created"
    success_url = reverse_lazy('sandwich')


class SandwichesUpdateView(LoginRequiredMixin, UpdateView):
    model = Sandwich
    fields = ['name', 'description', 'image', 'price']
    template_name = 'menu/update_sandwich.html'
    success_message = "sandwich has been updated"
    success_url = reverse_lazy('sandwich')


class SandwichesDeleteView(LoginRequiredMixin, DeleteView):
    model = Sandwich
    template_name = 'menu/delete-sandwich.html'
    success_message = "sandwich has been deleted"
    success_url = reverse_lazy('sandwich')


# Cakes menu
class CakesListView(ListView):
    model = Cake
    queryset = Cake.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/cake.html'


class CakesCreateView(LoginRequiredMixin, CreateView):
    model = Cake
    fields = ['name', 'description', 'image', 'price']
    template_name = 'menu/create_cake.html'
    success_message = "Cake created"
    success_url = reverse_lazy('cakes')


class CakesUpdateView(LoginRequiredMixin, UpdateView):
    model = Cake
    fields = ['name', 'description', 'image', 'price']
    template_name = 'menu/update_cake.html'
    success_message = "Cake has been updated"
    success_url = reverse_lazy('cakes')


class CakesDeleteView(LoginRequiredMixin, DeleteView):
    model = Cake
    template_name = 'menu/delete-cake.html'
    success_message = "Cake has been deleted"
    success_url = reverse_lazy('cakes')
