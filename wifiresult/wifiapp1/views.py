from django.shortcuts import render
from django.http import HttpResponse
from wifiapp1.models import Result, Job
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    results=Result.objects.all()
    jobs=Job.objects.all()
    return render(request, 'mainfile/index.html',{'results': results, 'jobs': jobs})

def results(request):
    results=Result.objects.all()
    return render(request, 'mainfile/results.html',{'results': results})

def admitcards(request):
    # Render the admitcards.html template
    return render(request, 'mainfile/admitcards.html')

def answerkey(request):
    # Render the answerkey.html template
    return render(request, 'mainfile/answerkeys.html')

def jobs(request):
    jobs=Job.objects.all()
    return render(request, 'mainfile/jobs.html', {'jobs': jobs})

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


def resultpost(request, slug):
    result = get_object_or_404(Result, slug=slug)
    return render(request, "result/resultslug.html", {"result": result,})


def jobpost(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, "job/jobslug.html", {"job": job,})


