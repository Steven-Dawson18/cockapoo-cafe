from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Models for Hot Drinks Menu
    """
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200, default=name)
    description = models.TextField(blank=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.FloatField()
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='menuitems', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name
