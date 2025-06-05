from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['index', 'results', 'admitcards', 'answerkeys', 'jobs', 'syllabus', 'about', 'contact', 'search', 'privacy']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'index':
            return 1.0
        elif item == 'contact':
            return 0.8
        else:
            return 0.8  # default priority for other static pages