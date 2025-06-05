from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # Render the index.html template
    return render(request, 'mainfile/index.html')

def results(request):
    # Render the results.html template
    return render(request, 'mainfile/results.html')

def admitcards(request):
    # Render the admitcards.html template
    return render(request, 'mainfile/admitcards.html')

def answerkey(request):
    # Render the answerkey.html template
    return render(request, 'mainfile/answerkeys.html')

def jobs(request):
    # Render the jobs.html template
    return render(request, 'mainfile/jobs.html')

def syllabus(request):
    # Render the syllabus.html template
    return render(request, 'mainfile/syllabus.html')

def about(request):
    # Render the about.html template
    return render(request, 'mainfile/about.html')

def contact(request):
    # Render the contact.html template
    return render(request, 'mainfile/contact.html')

def search(request):
    # Render the search.html template
    return render(request, 'mainfile/search.html')

def privacy(request):
    # Render the privacy.html template
    return render(request, 'mainfile/privacy.html')