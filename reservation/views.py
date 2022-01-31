'''Reservation views'''
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.forms.widgets import SelectDateWidget
from django.contrib import messages
from django.db.models import Q
from .models import Reservation


def error_404_view(request, exception):
    return render(request, '404.html')


class ReservationListView(LoginRequiredMixin, ListView):
    '''
    View to show the reservations that have been made
    Logged in user can only see their reservation but admin can see all
    There is a traffic light system to show if the reservation is pending,
    confirmed or rejected by the admin.
    '''
    model = Reservation
    queryset = Reservation.objects.all().order_by('datetime')
    template_name = 'reservation/reservation.html'


class ReservationApproveListView(LoginRequiredMixin, ListView):
    '''
    View to show all pending reservations to the admin only.
    From here they can accept or reject the reservation.
    '''
    model = Reservation
    queryset = Reservation.objects.filter(
        Q(accepted=False) & Q(rejected=False))
    template_name = 'reservation/approve-reservation.html'


class ReservationCreateView(LoginRequiredMixin, SuccessMessageMixin,
                            CreateView):
    '''
    View displays the form to create a reservation to the user.
    They must be logged in to make a reservation and will receive a message
    of success when submitted. A date selector has been added for the users
    convenience and the form is validated for phone, email and date.
    '''
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime',
              'information']
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


class ReservationUpdateView(LoginRequiredMixin, SuccessMessageMixin,
                            UpdateView):
    '''
    View displays the form to update a reservation to the user.
    They must be logged in to update a reservation and will receive a message
    of success when submitted. A date selector has been added for the users
    convenience and the form is validated for phone, email and date.
    '''
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime',
              'information']
    template_name = 'reservation/update_reservation.html'
    success_message = "Reservation will be updated"
    success_url = reverse_lazy('reservation')

    # Adapted from stackoverflow
    def get_form(self, form_class=None):
        '''add date picker in Update forms'''
        form = super(ReservationUpdateView, self).get_form(form_class)
        form.fields['datetime'].widget = SelectDateWidget()
        return form

    def get(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        return super(ReservationUpdateView, self).get(request, pk,
                                                      *args, **kwargs)

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        reseervation = Reservation.objects.get(pk=pk)
        reseervation.accepted = False
        reseervation.save()
        messages.success(request,
                         'The Reservation has been sent for approval')
        return super(ReservationUpdateView,
                     self).post(request, pk, *args, **kwargs)


class ReservationDeleteView(LoginRequiredMixin, SuccessMessageMixin,
                            DeleteView):
    '''
    View displays the option to delete the reservation to the user.
    '''
    model = Reservation
    fields = ['first_name', 'last_name', 'email', 'phone', 'time', 'datetime',
              'information']
    template_name = 'reservation/delete_reservation.html'
    success_message = "Reservation will be deleted"
    success_url = reverse_lazy('reservation')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReservationDeleteView,
                     self).delete(request, *args, **kwargs)


def approved_reservation(request, pk):
    '''View gives the option to approve the reservation to the admin.'''
    reservation = Reservation.objects.get(pk=pk)
    reservation.accepted = True
    reservation.save()
    messages.success(request, 'The Reservation was Accepted.')
    return HttpResponseRedirect(reverse('approve_reservation'))


def reject_reservation(request, pk):
    '''View gives the option to reject the reservation to the admin.'''
    reservation = Reservation.objects.get(pk=pk)
    reservation.rejected = True
    reservation.save()
    messages.success(request, 'The Reservation was rejected.')
    return HttpResponseRedirect(reverse('approve_reservation'))
