"""
Testing views in the Review app
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.messages import get_messages
from .models import Reservation


User = get_user_model()


class TestReservationViews(TestCase):
    """
    Test views in Reservation app
    """
    def setUp(self):
        """
        Set up users for the tests
        """
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = False
        user_a.save()
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', 'cfe3@invlalid.com',
                                          'some_123_password')
        self.user_b = user_b

    def test_user_count(self):
        """
        Check users are set up
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_reservation_list_view(self):
        """
        Test that logged in users can view the reservations page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get('/reservation/')
        self.assertTemplateUsed(response, 'reservation/reservation.html')
        self.assertEqual(response.status_code, 200)

    def test_superuser_reservation_list_view(self):
        """
        Test that superuser can view the reservations page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get('/reservation/')
        self.assertTemplateUsed(response, 'reservation/reservation.html')
        self.assertEqual(response.status_code, 200)

    def test_reservation_create_view(self):
        """
        Test that logged in users can create a reservation
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get('/reservation/create_reservation/')
        self.assertTemplateUsed(response,
                                'reservation/create_reservation.html')
        self.assertEqual(response.status_code, 200)

    def test_superuser_reservation_create_view(self):
        """
        Test that superusers can create a reservation
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get('/reservation/create_reservation/')
        self.assertTemplateUsed(response,
                                'reservation/create_reservation.html')
        self.assertEqual(response.status_code, 200)

    def test_non_user_reservation_create_view(self):
        """
        Test that non logged in users can't create a reservation
        """
        response = self.client.get('/reservation/create_reservation/')
        self.assertNotEqual(response.status_code, 200)
