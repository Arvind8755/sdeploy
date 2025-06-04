from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('admitcards/', views.admitcards, name='admitcards'),
    path('answerkeys/', views.answerkey, name='answerkeys'),
    path('jobs/', views.jobs, name='jobs'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]  
