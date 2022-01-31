from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .models import Category, MenuItem

class TestGetCategories(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_url = reverse('menu')

    def test_one_categories_should_return_exists(self):
        test_category = Category.objects.create(name="test_category")
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, 200)
        print(test_category.name)
