from django.shortcuts import render
from django.conf import settings


def home(request):
    return render(request, "home/home.html")


def contact(request):

    GOOGLE_MAPS_API = settings.GOOGLE_MAPS_API
    context = {"GOOGLE_MAPS_API": GOOGLE_MAPS_API}
    return render(request, "home/contact.html", context)
