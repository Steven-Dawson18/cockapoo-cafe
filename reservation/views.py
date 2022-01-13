from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Reservation, Reservation_Choices
from django.forms.widgets import SelectDateWidget
from django.contrib import messages
from django.db.models import Q


class ReservationListView(ListView):
    model = Reservation
    queryset = Reservation.objects.all().order_by('datetime')
    template_name = 'reservation/reservation.html'
    paginate_by = 6


class ReservationApproveListView(ListView):
    model = Reservation
    queryset = Reservation.objects.filter(Q(accepted=False) & Q(rejected=False))
    template_name = 'reservation/approve-reservation.html'


class ReservationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime', 'information']
    template_name = 'reservation/create_reservation.html'
    success_message = "Reservation created, will be approve soon"
    success_url = reverse_lazy('reservation')

    # Adapted from stackoverflow
    def get_form(self, form_class=None):
        '''add date picker in Create forms'''
        form = super(ReservationCreateView, self).get_form(form_class)
        form.fields['datetime'].widget = SelectDateWidget()
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_notification(request):
    #     """
    #     Function that count new reservations
    #     """
    #     reservation_count = Reservation.objects.filter(accepted=True).count()
       
    #     return reservation_count


class ReservationUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime', 'information']
    template_name = 'reservation/update_reservation.html'
    success_message = "Reservation will be updated"
    success_url = reverse_lazy('reservation')

    # Adapted from stackoverflow
    def get_form(self, form_class=None):
        '''add date picker in Update forms'''
        form = super(ReservationUpdateView, self).get_form(form_class)
        form.fields['datetime'].widget = SelectDateWidget()
        form.fields['datetime'].widget = SelectDateWidget()
        return form

    # def getReservationApproval(request, pk):
    #     reservation = Reservation.objects.get(pk=pk)
    #     reservation.accepted = False
    #     reservation.save()
    #     return reservation


class ReservationDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime', 'information']
    template_name = 'reservation/delete_reservation.html'
    success_message = "Reservation will be deleted"
    success_url = reverse_lazy('reservation')


def approvedReservation(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.accepted = True
    reservation.save()
    messages.success(request, 'The Reservation was Accepted.')
    return HttpResponseRedirect(reverse('approve_reservation'))


def rejectReservation(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.rejected = True
    reservation.save()
    messages.success(request, 'The Reservation was rejected.')
    return HttpResponseRedirect(reverse('approve_reservation'))
