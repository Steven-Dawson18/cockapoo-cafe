from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReservationListView.as_view(), name="reservation"),
    path('create_reservation/', views.ReservationCreateView.as_view(), name="create_reservation"),
]
