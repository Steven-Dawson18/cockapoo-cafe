"""
Testing models in the Review app
"""

from django.test import TestCase
from .models import Review
from django.contrib.auth import get_user_model


User = get_user_model()


class TestReviewModel(TestCase):
    """
    Test Review model returns Reservation name as string
    """

    def test_review_string_method_returns_author(self):
        """
        Test model returns Review name as string
        """
        user_b = User.objects.create_user('test_reservation_name', 'test_reservation_surname', 'cfe3@invlalid.com')
        self.user_b = user_b
        review = Review.objects.create(
            author=user_b,
            title="TestTitle",
            body="TestBody",
            image="TestImage",
            created_on='2022-02-01',
            updated_on= '2022-02-01',
            status='0',
            approved='False')
        self.assertEqual(str(review), 'Comment TestBody by test_reservation_name')
