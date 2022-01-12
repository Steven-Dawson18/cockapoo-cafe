from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReservationListView.as_view(), name="reservation"),
    path('create_reservation/', views.ReservationCreateView.as_view(), name="create_reservation"),
    path('update_reservation/<pk>/', views.ReservationUpdateView.as_view(), name="update_reservation"),
    path('delete_reservation/<pk>/', views.ReservationDeleteView.as_view(), name='delete_reservation'),
    path('approve_reservation/', views.ReservationApproveListView.as_view(), name='approve_reservation'),
    path('approve_reservation/<pk>', views.approvedReservation, name='approved_revservation'),
]
