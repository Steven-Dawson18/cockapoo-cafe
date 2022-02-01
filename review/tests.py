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
        Set up users and review for the tests
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

        self.review_a = Review.objects.create(
            author=user_b,
            title="TestTitle",
            body="TestBody",
            image="TestImage",
            created_on='2022-02-01',
            updated_on='2022-02-01',
            status='0',
            approved='False')

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
        Test that a logged in user can access the create a review page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.post("/review/create_review/")
        self.assertEqual(response.status_code, 200)

    def test_admin_valid_request(self):
        """
        Test that a logged in superuser can access the create a review page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.post("/review/create_review/")
        self.assertEqual(response.status_code, 200)

    def test_invalid_request(self):
        """
        Test that a non logged in user can't access the create a review page
        """
        response = self.client.post("/review/create_review/")
        self.assertEqual(response.status_code, 302)

    def test_edit_review_view(self):
        """
        Test that only the author can edit the review.
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get(f'/review/update_review/{self.review_a.id}/')
        # self.assertNotEqual(self.review_a.author.id, self.user_a.id)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Unauthorised.')
        self.assertEqual(response.status_code, 302)
