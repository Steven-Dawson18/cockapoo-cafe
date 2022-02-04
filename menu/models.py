'''Menu Models'''
from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


User = get_user_model()

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Models for Menu Category
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Models for Menu Item
    """
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.FloatField(default=3.99)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='menuitems', blank=True)

    class Meta:
        """Models ordering"""
        ordering = ["-created_on"]

    def total_likes(self):
        """Function to count likes"""
        return self.likes.count()

    def __str__(self):
        return self.name
