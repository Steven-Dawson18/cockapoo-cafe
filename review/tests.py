"""
Testing views in the Review app
"""

from django.test import TestCase

from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from .models import Review


class TestReviewViews(TestCase):
    """
    Test views in Review app
    """
    # def setUp(self):
    #     """
    #     Set up info needed for testing
    #     """
    #     self.admin_user = User.objects.create_superuser(
    #         username='admin',
    #         password='1234',
    #         email='admin@test.com',
    #     )

    #     self.user = User.objects.create_user(
    #         username='user',
    #         password='1234',
    #         email='user@test.com',
    #     )

    #     self.user = User.objects.get(username="tester")

    #     self.review1 = Review.objects.create(
    #         author='reviewerName1',
    #         title='test',
    #         body='test',
    #         image='test',
    #         created_on='test',
    #         updated_on='test',
    #         status='1',
    #         approved='test',
    #         likes='test'
    #     )

    def test_Review_List_view(self):
            """
            Test that all users can view all approved reviews page
            """
            response = self.client.get('/review/')
            self.assertTemplateUsed(response, 'review/review.html')
            self.assertEqual(response.status_code, 200)