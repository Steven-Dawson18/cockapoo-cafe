from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name="menu"),
    path('hot-drinks/', views.HotDrinksList.as_view(), name="hot-drinks"),
    path('cold-drinks/', views.ColdDrinksList.as_view(), name="cold-drinks"),
    path('sandwiches/', views.SandwichList.as_view(), name="Sandwich"),
     path('cakes/', views.CakeList.as_view(), name="cakes"),
]
