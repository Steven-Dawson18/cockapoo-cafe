from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewListView.as_view(), name="review"),
    path('manage_review/', views.ManageReviewList.as_view(), name="manage_review"),
    path('update_review/<pk>/', views.ReviewUpdateView.as_view(), name="update_review"),
    path('create_review/', views.ReviewCreateView.as_view(), name='create_review'),
    path('delete_review/<pk>/', views.ReviewDeleteView.as_view(), name='delete_review'),
    path('review_like/<pk>', views.LikeView, name="like-review"),
]
