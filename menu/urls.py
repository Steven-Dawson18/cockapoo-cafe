from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuListView.as_view(), name="menu"),
    # path('menulist/', views.MenuList.as_view(), name="menu-list"),
    path('hot-drinks/', views.HotDrinksListView.as_view(), name="hot-drinks"),
    path('create-hot-drinks/', views.HotdrinksCreateView.as_view(), name="create-hot-drinks"),
    path('update-hot-drinks/<pk>/', views.HotdrinksUpdateView.as_view(), name="update-hot-drink"),
    path('delete-hot-drinks/<pk>/', views.HotdrinksDeleteView.as_view(), name="delete-hot-drink"),
    path('cold-drinks/', views.ColdDrinksListView.as_view(), name="cold-drinks"),
    path('create-cold-drinks/', views.ColdDrinksCreateView.as_view(), name="create-cold-drinks"),
    path('update-cold-drinks/<pk>/', views.ColdDrinksUpdateView.as_view(), name="update-cold-drink"),
    path('delete-cold-drinks/<pk>/', views.ColdDrinksDeleteView.as_view(), name="delete-cold-drink"),
    path('sandwiches/', views.SandwichList.as_view(), name="Sandwich"),
    path('cakes/', views.CakeList.as_view(), name="cakes"),
]
