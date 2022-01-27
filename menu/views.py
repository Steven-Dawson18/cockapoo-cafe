'''Menu views'''
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .models import MenuItem, Category


class CategoryMenuListView(ListView):
    '''View to show all categories of menu items'''
    Model = Category
    queryset = Category.objects.all()
    template_name = 'menu/menu.html'


class CategoryMenuItemListView(ListView):
    '''
    View to show the menu for each category
    User is able to like the menu items if they are logged in.
    '''
    paginate_by = 10
    template_name = 'menu/categories.html'
    model = MenuItem
    context_object_name = 'menuitem'

    def get_queryset(self):
        '''Function to show the menu item in each category list'''
        return MenuItem.objects.filter(category_id=self.kwargs['pk'])

    def get_context(self):
        '''
        Function gives the user the ability to like a menu item.
        '''
        item = get_object_or_404(MenuItem, id=self.pk)
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=self.request.user.id).exists():
            liked = True
            context["total_likes"] = total_likes
            context["liked"] = liked
        return context


class AddCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin,
                            CreateView):
    '''
    View displays the form to create a menu category to the admin.
    They must be logged in to create a category and will receive a message
    of success when created.
    '''
    model = Category
    template_name = 'menu/add_menu_category.html'
    fields = '__all__'
    success_message = "Category created"
    success_url = reverse_lazy('menu')


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    '''
    View displays the form to update a category to the admin.
    They must be logged in to update a category and will receive a message
    of success when submitted.
    '''
    model = Category
    fields = '__all__'
    template_name = 'menu/update-category.html'
    success_message = "Category has been updated"
    success_url = reverse_lazy('menu')


class CategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    '''
    View displays the option to delete the category to the admin.
    '''
    model = Category
    template_name = 'menu/delete-category.html'
    success_message = "Category has been deleted"
    success_url = reverse_lazy('menu')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CategoryDeleteView, self).delete(request, *args, **kwargs)


class MenuViewMenuListView(SuccessMessageMixin, ListView):
    '''
    View to show all items of the menus
    Only visbale to the admin who can create, edit and delete
    menu items from here.
    '''
    Model = MenuItem
    queryset = MenuItem.objects.all().order_by('category')
    template_name = 'menu/menu-items.html'
    success_message = "Item created"
    success_url = reverse_lazy('menu-items')


class AddMenuItemCreateView(LoginRequiredMixin, SuccessMessageMixin,
                            CreateView):
    '''
    View displays the form to create a menu Item to the admin.
    They must be logged in to create a menu Item and will receive a message
    of success when created.
    '''
    model = MenuItem
    template_name = 'menu/create-menu-item.html'
    fields = ['name', 'description', 'image', 'category', 'price']
    success_message = "Menu Item Created"
    success_url = reverse_lazy('menu-items')


class MenuItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    '''
    View displays the form to update a menu Item to the admin.
    They must be logged in to update a menu Item and will receive a message
    of success when submitted.
    '''
    model = MenuItem
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = 'menu/update-menu-item.html'
    success_message = "Menu Item has been updated"
    success_url = reverse_lazy('menu-items')


class MenuItemDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    '''
    View displays the option to delete the menu Item to the admin.
    '''
    model = MenuItem
    template_name = 'menu/delete-menu-item.html'
    success_message = "Menu Item has been deleted"
    success_url = reverse_lazy('menu-items')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MenuItemDeleteView, self).delete(request, *args, **kwargs)


def like_view(request, pk):
    '''
    Function gives the user the ability to like a Menu Item.
    '''
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
