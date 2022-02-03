"""
Testing views in the Menu app
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Category, MenuItem


User = get_user_model()


class TestMenuViews(TestCase):
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
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', 'cfe3@invlalid.com',
                                          'some_123_password')
        self.user_b = user_b

        self.cat1 = Category.objects.create(name='test_category_name')
        self.item1 = MenuItem.objects.create(
            name='test_item_name',
            category=self.cat1,
            description='test_discription',
            image='test_image',
            price='3.99',
            status='1',
            created_on='2022-02-01',
            updated_on='2022-02-01')

    def test_user_count(self):
        """
        Check users are set up
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_menu_list_view(self):
        """
        Test that all users can view the main menu page
        """
        response = self.client.get('/menu/')
        self.assertTemplateUsed(response, 'menu/menu.html')
        self.assertEqual(response.status_code, 200)

    def test_menu_category_list_view(self):
        """
        Test that all users can view the category menu pages
        """
        response = self.client.get(f'/menu/category/{self.item1.id}/')
        self.assertTemplateUsed(response, 'menu/categories.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_menu_not_accessed_by_non_admin(self):
        """
        Test that logged in users can not view the admin only menu item page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get('/menu/menu-items/')
        self.assertTemplateUsed(response, '403.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_menu_access_by_admin(self):
        """
        Test that admin users can view the admin only menu item page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get('/menu/menu-items/')
        self.assertTemplateUsed(response, 'menu/menu-items.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_create_menu_item_not_accessed_by_non_admin(self):
        """
        Test that logged in users can not view the admin only create
        menu item page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get('/menu/create-menu-item/')
        self.assertTemplateUsed(response, '403.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_create_menu_item_access_by_admin(self):
        """
        Test that admin users can view the admin only menu item page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get('/menu/create-menu-item/')
        self.assertTemplateUsed(response, 'menu/create-menu-item.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_update_menu_item_not_accessed_by_non_admin(self):
        """
        Test that logged in users can not view the admin only update
        menu item page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get(f'/menu/update-menu-item/{self.item1.id}/')
        self.assertTemplateUsed(response, '403.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_update_menu_item_access_by_admin(self):
        """
        Test that admin users can view the admin only update
        menu item page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get(f'/menu/update-menu-item/{self.item1.id}/')
        self.assertTemplateUsed(response, 'menu/update-menu-item.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_udelete_menu_item_not_accessed_by_non_admin(self):
        """
        Test that logged in users can not view the admin only delete
        menu item page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get(f'/menu/delete-menu-item/{self.item1.id}/')
        self.assertTemplateUsed(response, '403.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_menu_item_access_by_admin(self):
        """
        Test that admin users can view the admin only delete
        menu item page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get(f'/menu/delete-menu-item/{self.item1.id}/')
        self.assertTemplateUsed(response, 'menu/delete-menu-item.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_create_category_not_accessed_by_non_admin(self):
        """
        Test that logged in users can not view the admin only create
        category page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get('/menu/create-menu-category/')
        self.assertTemplateUsed(response, '403.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_create_category_access_by_admin(self):
        """
        Test that admin users can view the admin only create category page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get('/menu/create-menu-category/')
        self.assertTemplateUsed(response, 'menu/add_menu_category.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_update_category_not_accessed_by_non_admin(self):
        """
        Test that logged in users can not view the admin only update
        category page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get(f'/menu/update-category/{self.cat1.id}/')
        self.assertTemplateUsed(response, '403.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_update_category_access_by_admin(self):
        """
        Test that admin users can view the admin only update category page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get(f'/menu/update-category/{self.cat1.id}/')
        self.assertTemplateUsed(response, 'menu/update-category.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_category_not_accessed_by_non_admin(self):
        """
        Test that logged in users can not view the admin only delete
        category page
        """
        self.client.login(username=self.user_b.username,
                          password='some_123_password')
        response = self.client.get(f'/menu/delete-category/{self.cat1.id}/')
        self.assertTemplateUsed(response, '403.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_category_access_by_admin(self):
        """
        Test that admin users can view the admin only delete category page
        """
        self.client.login(username=self.user_a.username,
                          password='some_123_password')
        response = self.client.get(f'/menu/delete-category/{self.cat1.id}/')
        self.assertTemplateUsed(response, 'menu/delete-category.html')
        self.assertEqual(response.status_code, 200)
