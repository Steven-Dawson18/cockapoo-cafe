"""
Testing models in the Reservation app
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Reservation


User = get_user_model()


class TestReservationModel(TestCase):
    """
    Test Reservation model returns Reservation name as string
    """
    def setUp(self):
        """
        Set up users for the tests
        """
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', 'cfe3@invlalid.com',
                                          'some_123_password')
        self.user_b = user_b

    def test_string_method_returns_name(self):
        """
        Test model returns Reservation name as string
        """
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
