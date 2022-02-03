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
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', 'cfe3@invlalid.com',
                                          'some_123_password')
        self.user_b = user_b

        self.reservation1 = Reservation.objects.create(
            first_name='testName',
            last_name='testSurname',
            email='cfe@invalid.com',
            phone='07564654321',
            time='12pm',
            datetime='2022-02-01',
            information='test',
            sent_date='2022-02-01',
            accepted='False',
            rejected='False',
            accepted_date='2022-02-01',
            user=self.user_a
        )

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
        Test that logged in users can access create reservation page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get('/reservation/create_reservation/')
        self.assertTemplateUsed(response,
                                'reservation/create_reservation.html')
        self.assertEqual(response.status_code, 200)

    def test_superuser_reservation_create_view(self):
        """
        Test that superusers can access create reservation page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get('/reservation/create_reservation/')
        self.assertTemplateUsed(response,
                                'reservation/create_reservation.html')
        self.assertEqual(response.status_code, 200)

    def test_non_user_reservation_create_view(self):
        """
        Test that non logged in users can't access create reservation page
        """
        response = self.client.get('/reservation/create_reservation/')
        self.assertNotEqual(response.status_code, 200)

    def test_edit_reservation_view(self):
        """
        Test that only the person who made the reservation can edit.
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get(
            f'/reservation/update_reservation/{self.reservation1.id}/')
        self.assertNotEqual(self.reservation1.user.id, self.user_b.id)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Unauthorised!')
        self.assertEqual(response.status_code, 302)

    def test_admin_approve_reservation_access_by_admin(self):
        """
        Test that admin users can view the admin only approve
        reservation page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get('/reservation/approve_reservation/')
        self.assertTemplateUsed(
            response, 'reservation/approve-reservation.html')
        self.assertEqual(response.status_code, 200)
