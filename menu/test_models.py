"""
Testing models in the products app
"""

from django.test import TestCase
from .models import Category, MenuItem


class TestCategoryModel(TestCase):
    """
    Test category model returns category name as string
    """

    def test_string_method_returns_name(self):
        """
        Test model returns category name as string
        """
        category = Category.objects.create(name='test_category_name')
        self.assertEqual(str(category), 'test_category_name')


# class TestMenuItemModel(TestCase):
#     """
#     Test MenuItem model returns Menu Item name as string
#     """

#     def test_string_method_returns_name(self):
#         """
#         Test model returns Menu Item name as string
#         """
#         item = MenuItem.objects.create(name='test_item_name')
#         self.assertEqual(str(item), 'test_item_name')
