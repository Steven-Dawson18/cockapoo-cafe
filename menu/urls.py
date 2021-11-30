from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name="menu"),
    path('hot-drinks/', views.HotDrinksList.as_view(), name="hot-drinks"),
]
