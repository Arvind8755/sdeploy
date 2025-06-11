from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Result, Job

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['index', 'results', 'admitcards', 'answerkeys', 'jobs', 'syllabus', 'about', 'contact', 'search', 'privacy']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'index':
            return 1.0000
        elif item == 'contact':
            return 0.8000
        else:
            return 0.8  # default priority for other static pages
        
class ResultSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8000

    def items(self):
        return Result.objects.filter(active=True)

    def location(self, obj):
        return obj.get_absolute_url()

class JobSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8000

    def items(self):
        return Job.objects.filter(active=True)

    def location(self, obj):
        return obj.get_absolute_url()