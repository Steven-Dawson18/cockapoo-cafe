from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList, name="menu"),
    path('hot-drinks/', views.HotDrinksListView.as_view(), name="hot-drinks"),
    path('create-hot-drinks/', views.HotdrinksCreateView.as_view(), name="create-hot-drinks"),
    path('update-hot-drinks/<pk>/', views.HotdrinksUpdateView.as_view(), name="update-hot-drink"),
    path('delete-hot-drinks/<pk>/', views.HotdrinksDeleteView.as_view(), name="delete-hot-drink"),
    path('cold-drinks/', views.ColdDrinksListView.as_view(), name="cold-drinks"),
    path('create-cold-drinks/', views.ColdDrinksCreateView.as_view(), name="create-cold-drinks"),
    path('update-cold-drinks/<pk>/', views.ColdDrinksUpdateView.as_view(), name="update-cold-drink"),
    path('delete-cold-drinks/<pk>/', views.ColdDrinksDeleteView.as_view(), name="delete-cold-drink"),
    path('sandwich/', views.SandwichesListView.as_view(), name="sandwich"),
    path('create-sandwich/', views.SandwichesCreateView.as_view(), name="create-sandwich"),
    path('update-sandwich/<pk>/', views.SandwichesUpdateView.as_view(), name="update-sandwich"),
    path('delete-sandwich/<pk>/', views.SandwichesDeleteView.as_view(), name="delete-sandwich"),
    path('cakes/', views.CakesListView.as_view(), name="cakes"),
    path('create-cake/', views.CakesCreateView.as_view(), name="create-cake"),
    path('update-cake/<pk>/', views.CakesUpdateView.as_view(), name="update-cake"),
    path('delete-cake/<pk>/', views.CakesDeleteView.as_view(), name="delete-cake"),
    path('like/<pk>', views.LikeView, name="like-hot-drink"),
    path('cold-like/<pk>', views.ColdLikeView, name="like-cold-drink"),
    path('cake-like/<pk>', views.CakeLikeView, name="like-cake"),
    path('sandwich-like/<pk>', views.SandwichLikeView, name="like-sandwich"),
]
