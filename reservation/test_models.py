"""
Testing models in the Reservation app
"""

from django.test import TestCase
from .models import Reservation


# class TestReservationModel(TestCase):
#     """
#     Test Reservation model returns Reservation name as string
#     """

#     def test_string_method_returns_name(self):
#         """
#         Test model returns Reservation name as string
#         """
#         reservation = Reservation.objects.create(ret='test_reservation_name')
#         self.assertEqual(str(reservation), 'test_reservation_name')
