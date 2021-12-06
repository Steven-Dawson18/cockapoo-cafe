from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="User"
    )
    title = models.CharField(max_length=200, default='no_title', null=True, blank=True)
    body = models.TextField()
    image = CloudinaryField('image', default='review_placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
