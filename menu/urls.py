'''Menu urls'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryMenuListView.as_view(), name="menu"),
    path('menu-items/', views.MenuViewMenuListView.as_view(),
         name="menu-items"),
    path('create-menu-category/', views.AddCategoryCreateView.as_view(),
         name="create-menu-category"),
    path('update-category/<pk>/', views.CategoryUpdateView.as_view(),
         name="update-category"),
    path('delete-category/<pk>/', views.CategoryDeleteView.as_view(),
         name="delete-category"),
    path('create-menu-item/', views.AddMenuItemCreateView.as_view(),
         name="create-menu-item"),
    path('update-menu-item/<pk>/', views.MenuItemUpdateView.as_view(),
         name="update-menu-item"),
    path('delete-menu-item/<pk>/', views.MenuItemDeleteView.as_view(),
         name="delete-menu-item"),
    path('category/<pk>/', views.CategoryMenuItemListView.as_view(),
         name='category'),
    path('category/like-menu-item/<pk>/', views.like_view,
         name="like-menu-item"),
]
