from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from .models import MenuItem, Category


class CategoryMenuListView(ListView):
    Model = Category
    queryset = Category.objects.all()
    template_name = 'menu/menu.html'


class CategoryMenuItemListView(ListView):
    paginate_by = 10
    template_name = 'menu/categories.html'
    model = MenuItem
    context_object_name = 'menuitem'

    def get_queryset(self):
        return MenuItem.objects.filter(category_id=self.kwargs['pk'])

    def get_context(self):
        item = get_object_or_404(MenuItem, id=self.pk)
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=self.request.user.id).exists():
            liked = True
            context["total_likes"] = total_likes
            context["liked"] = liked
        return context


class AddCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'menu/add_menu_category.html'
    fields = '__all__'
    success_message = "Category created"
    success_url = reverse_lazy('menu')


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'menu/update-category.html'
    success_message = "Category has been updated"
    success_url = reverse_lazy('menu')


class CategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'menu/delete-category.html'
    success_message = "Category has been deleted"
    success_url = reverse_lazy('menu')


class MenuViewMenuListView(SuccessMessageMixin, ListView):
    Model = MenuItem
    queryset = MenuItem.objects.all().order_by('category')
    template_name = 'menu/menu-items.html'
    success_message = "Item created"
    success_url = reverse_lazy('menu-items')


class AddMenuItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MenuItem
    template_name = 'menu/create-menu-item.html'
    fields = ['name', 'description', 'image', 'category', 'price']
    success_message = "Menu Item Created"
    success_url = reverse_lazy('menu-items')


class MenuItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MenuItem
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = 'menu/update-menu-item.html'
    success_message = "Menu Item has been updated"
    success_url = reverse_lazy('menu-items')


class MenuItemDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = MenuItem
    template_name = 'menu/delete-menu-item.html'
    success_message = "Menu Item has been deleted"
    success_url = reverse_lazy('menu-items')


def LikeView(request, pk):
    item = get_object_or_404(MenuItem, id=pk)
    category_id = item.category.id
    liked = False
    if item.likes.filter(id=request.user.id).exists():
        item.likes.remove(request.user)
        liked = False
    else:
        item.likes.add(request.user)
        liked = True
    return redirect(reverse('category', args=[category_id]))
