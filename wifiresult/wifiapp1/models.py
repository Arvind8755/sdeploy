from django.db import models

# Create your models here.

class Result(models.Model):
    title = models.CharField(max_length=250)
    admission_date = models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.title
    
class Admitcard(models.Model):
    title = models.CharField(max_length=250)
    admission_date = models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.title
    
class Answerkey(models.Model):
    title = models.CharField(max_length=250)
    admission_date = models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.title
    
class Job(models.Model):
    title = models.CharField(max_length=250)
    admission_date = models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.title
    
class Syllabus(models.Model):
    title = models.CharField(max_length=250)
    admission_date = models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.title