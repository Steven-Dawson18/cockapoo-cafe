'''Review Models'''
from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


User = get_user_model()


STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    """Models for review"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="User"
    )
    title = models.CharField(max_length=200, default='no_title', null=True,
                             blank=True)
    body = models.TextField()
    image = CloudinaryField('image', default='review_placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='reviews', blank=True)

    class Meta:
        """Models ordering"""
        ordering = ["created_on"]

    def total_likes(self):
        """Function to count likes"""
        return self.likes.count()

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
