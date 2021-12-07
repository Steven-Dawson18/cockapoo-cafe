from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation, name="reservation"),
    # path('', views.AuthorCreate.as_view(), name="author_create"),
]
