"""
Testing models in the Reservation app
"""

from django.test import TestCase
from .models import Reservation
from django.contrib.auth import get_user_model


User = get_user_model()


class TestReservationModel(TestCase):
    """
    Test Reservation model returns Reservation name as string
    """

    def test_string_method_returns_name(self):
        """
        Test model returns Reservation name as string
        """
        user_b = User.objects.create_user('test_reservation_name', 'test_reservation_surname', 'cfe3@invlalid.com')
        self.user_b = user_b
        reservation = Reservation.objects.create(
            first_name='John',
            last_name='Doe',
            email='cfe3@invlalid.com',
            phone='07564654321',
            time='12pm',
            datetime='2022-02-01',
            information='test',
            sent_date='2022-02-01',
            accepted='False',
            rejected='False',
            accepted_date='2022-02-01',
            user=self.user_b)
        self.assertEqual(str(reservation), 'John,Doe,cfe3@invlalid.com')
