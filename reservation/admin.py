""" Reservation admin.py"""
from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Filters, displays and search for django admin"""
    list_filter = ('accepted', 'sent_date', 'accepted')
    list_display = ('first_name', 'last_name', 'accepted_date', 'information',
                    'datetime', 'time')
    search_fields = ['datetime', 'time', 'accepted_date', 'last_name']
