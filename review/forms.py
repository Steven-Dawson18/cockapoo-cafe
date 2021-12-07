from . models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class meta:
        model = Review
        fields = ('body',)
