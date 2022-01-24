"""
Models for reservations
"""
from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models import Q, F


PHONE_MESSAGE = 'Please enter a valid number in the format: 07999999999'

Phone_Regex = RegexValidator(
        regex=r'^(07)\d{9}$',
        message=PHONE_MESSAGE
    )


Reservation_Choices = (
    ("9", "9am"),
    ("10", "10am"),
    ("11", "11am"),
    ("12", "12pm"),
    ("1", "1pm"),
    ("2", "2pm"),
    ("3", "3pm"),
    ("4", "4pm")
)


class Reservation(models.Model):
    """
    Models for reservations and user to be able to use foreign key
    """
    first_name = models.CharField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    email = models.EmailField(max_length=100, unique=False)
    phone = models.CharField(validators=[Phone_Regex], max_length=60,
                             null=True, blank=True)
    time = models.CharField(max_length=100, choices=Reservation_Choices,
                            default='9')
    datetime = models.DateField(auto_now_add=False, null=True, blank=False)
    information = models.TextField(blank=False,
                                   default='Please enter number of people:')
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        ret = self.first_name + ',' + self.last_name + ',' + self.email
        return ret

    def clean(self):
        now = datetime.now().date()
        if self.datetime <= now:
            raise ValidationError('The date cannot be in the past!')
        return super().clean()

    # Adapted from stackoverflow
    class Meta:
        """
        Sets the constraints and checks the date entered isn't in the past
        """
        ordering = ["datetime"]
