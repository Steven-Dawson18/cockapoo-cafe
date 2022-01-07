from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Menu, HotDrinks, ColdDrinks, Sandwich, Cake
from django.http import HttpResponseRedirect


# menu options
def MenuList(request):
    return render(request, "menu/menu.html")


# Hot drinks menu
class HotDrinksListView(ListView):
    model = HotDrinks
    queryset = HotDrinks.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/hot-drinks.html'

    def get_context(self):
        item = get_object_or_404(HotDrinks, id=self.pk)
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked

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
    liked = False
    if hotdrink.likes.filter(id=request.user.id).exists():
        hotdrink.likes.remove(request.user)
        liked = False
    else:
        hotdrink.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('hot-drinks'))


# Cold drinks menu
class ColdDrinksListView(ListView):
    model = ColdDrinks
    queryset = ColdDrinks.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/cold-drinks.html'

    def get_context(self):
        item = get_object_or_404(ColdDrinks, id=self.pk)
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context


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


def ColdLikeView(request, pk):
    colddrink = get_object_or_404(ColdDrinks, id=pk)
    liked = False
    if colddrink.likes.filter(id=request.user.id).exists():
        colddrink.likes.remove(request.user)
        liked = False
    else:
        colddrink.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('cold-drinks'))


# Sandwich menu
class SandwichesListView(ListView):
    model = Sandwich
    queryset = Sandwich.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/sandwich.html'

    def SandwichLikeView(request, pk):
        cake = get_object_or_404(Sandwich, id=pk)
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        
        return context


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


def SandwichLikeView(request, pk):
    sandwich = get_object_or_404(Sandwich, id=pk)
    liked = False
    if sandwich.likes.filter(id=request.user.id).exists():
        sandwich.likes.remove(request.user)
        liked = False
    else:
        sandwich.likes.add(request.user)
        liked = True
   
    return HttpResponseRedirect(reverse('sandwich'))


# Cakes menu
class CakesListView(ListView):
    model = Cake
    queryset = Cake.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu/cake.html'

    def get_context(self):
        item = get_object_or_404(Cake, id=self.pk)
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        
        return context


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


def CakeLikeView(request, pk):
    cake = get_object_or_404(Cake, id=pk)
    liked = False
    if cake.likes.filter(id=request.user.id).exists():
        cake.likes.remove(request.user)
        liked = False
    else:
        cake.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('cakes'))
