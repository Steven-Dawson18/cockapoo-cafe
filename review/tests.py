"""
Testing views in the Review app
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.messages import get_messages
from .models import Review


User = get_user_model()


class TestReviewViews(TestCase):
    """
    Test views in Review app
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

    def test_review_list_view(self):
        """
        Test that all users can view all approved reviews page
        """
        response = self.client.get('/review/')
        self.assertTemplateUsed(response, 'review/review.html')
        self.assertEqual(response.status_code, 200)

    def test_valid_request(self):
        """
        Test that a logged in user can create a reviews
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.post("/review/create_review/",
                                    {"title": "this is an valid test"})
        self.assertEqual(response.status_code, 200)

    def test_admin_valid_request(self):
        """
        Test that a logged in superuser can create a review
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.post("/review/create_review/",
                                    {"title": "this is a valid test"})
        self.assertEqual(response.status_code, 200)

    def test_invalid_request(self):
        """
        Test that a non logged in user can't create a review
        """
        response = self.client.post("/review/create_review/",
                                    {"title": "this is not a valid test"})
        self.assertEqual(response.status_code, 302)
