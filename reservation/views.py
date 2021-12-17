from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Reservation, Reservation_Choices


class ReservationListView(ListView):
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime', 'information']
    template_name = 'reservation/reservation.html'


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime', 'information']
    template_name = 'reservation/create_reservation.html'
    success_message = "Reservation created, will be approve soon"
    success_url = reverse_lazy('reservation')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime', 'information']
    template_name = 'reservation/update_reservation.html'
    success_message = "Reservation will be updated"
    success_url = reverse_lazy('reservation')


class ReservationDeleteView(DeleteView):
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime', 'information']
    template_name = 'reservation/delete_reservation.html'
    success_message = "Reservation will be deleted"
    success_url = reverse_lazy('reservation')
