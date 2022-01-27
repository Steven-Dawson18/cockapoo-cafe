from django.test import TestCase
from django.contrib.messages import get_messages


class TestHomeViews(TestCase):
    """
    Test the home view page
    """
    def test_page_access(self):
        """
        Test the home view page
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TestContactViews(TestCase):
    """
    Test contact page views
    """

    def test_contact_us_view(self):
        """
        Test that contact page is accessible
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_us_form(self):
        """
        Test that contact form is sent
        """
        message_name = 'test name'
        emailaddress = 'test@test.com'
        message = 'test message'

        data = {
            'message-name': message_name,
            'emailaddress': emailaddress,
            'message': message
        }

        response = self.client.post('/contact/', data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Email received. We will contact you shortly.')
