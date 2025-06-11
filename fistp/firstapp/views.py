from django.shortcuts import render
from django.http import HttpResponse

from django.template import Context, loader

from .models import Contact
from django.contrib import messages


from .forms import ContactForm

def home(request):
    return render(request, "amp.html")

def contact_view(request):
    message = ''
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Your message has been successfully sent."
        else:
            message = "Please fill the form correctly."

    return render(request, 'contact.html', {'form': form, 'message': message})