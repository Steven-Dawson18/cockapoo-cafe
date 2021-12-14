from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewList.as_view(), name="review"),
    path('manage_review/', views.ManageReviewList.as_view(), name="manage_review"),
    path('approve_review/', views.CreateReview.as_view(), name="approve_review"),
    path('update_review/', views.ManageReviewList.as_view(), name="update_review"),
    path('create_review/', views.CreateReview.as_view(), name='create_review'),
]
