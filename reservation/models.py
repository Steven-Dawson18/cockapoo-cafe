from django.db import models
from django.contrib.auth.models import User


Reservation_Choices = (
    ("10am", "4"),
    ("12am", "4"),
    ("2pm", "4"),
    ("4pm", "4")
)

# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)


# class Reservation(models.Model):
#     """
#     Models for reservations and user to be able to use foreign key
#     """
#     first_name = models.CharField(max_length=100, unique=False)
#     last_name = models.CharField(max_length=100, unique=False)
#     email = models.EmailField(max_length=100, unique=False)
#     phone = models.CharField(max_length=50, unique=False)
#     time = models.CharField(max_length=100, choices=Reservation_Choices,
#                                  default='4pm')
#     datetime = models.DateField(auto_now_add=False, null=True, blank=False)
#     information = models.TextField(blank=True)
#     sent_date = models.DateField(auto_now_add=True)
#     accepted = models.BooleanField(default=True)
#     accepted_date = models.DateTimeField(auto_now=True, null=True,
#                                          auto_now_add=True,)
#     user = models.ForeignKey(User, blank=True, null=True,
#                              on_delete=models.CASCADE)

#     # Define string representation for this model class,
#     # It will be used when display model class data in Django Admin web site.
#     def __str__(self):
#         ret = self.first_name + ',' + self.last_name + ',' + self.email
#         return ret

#     class Meta:
#         ordering = ["-sent_date"]
