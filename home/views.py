'''Home views'''
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def error_404_view(request, exception):
    '''404 error view'''
    return render(request, '404.html')


def home(request):
    '''Home page view'''
    return render(request, "home/home.html")


def contact(request):
    '''Contact page view'''
    GOOGLE_MAPS_API = settings.GOOGLE_MAPS_API
    context = {"GOOGLE_MAPS_API": GOOGLE_MAPS_API}
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['emailaddress']
        message = request.POST['message']

        send_mail('message from ' + message_name,
                  message + ' reply to this message ' + message_email,
                  message_email,
                  ['fullstacksteve18@gmail.com'])
        messages.success(request,
                         'Email received. We will contact you shortly.')
        return render(request, "home/contact.html", context)
    else:
        return render(request, "home/contact.html", context)
