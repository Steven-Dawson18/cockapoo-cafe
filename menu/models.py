from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Menu(models.Model):
    """
    Models for menu
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default=name)
    description = models.TextField(blank=False)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name


class HotDrinks(models.Model):
    """
    Models for Hot Drinks Menu
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default=name)
    description = models.TextField(blank=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.FloatField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name


class ColdDrinks(models.Model):
    """
    Models for Cold Drinks Menu
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default=name)
    description = models.TextField(blank=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.FloatField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    """
    Models for Sandwiches Menu
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default=name)
    description = models.TextField(blank=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.FloatField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name


class Cake(models.Model):
    """
    Models for Cakes Menu
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default=name)
    description = models.TextField(blank=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.FloatField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
