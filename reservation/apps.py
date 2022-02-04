""" Reservation apps.py"""
from django.apps import AppConfig


class ReservationConfig(AppConfig):
    """
    Reservation config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservation'
