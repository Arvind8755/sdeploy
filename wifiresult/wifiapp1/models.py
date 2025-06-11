from django.db import models
# from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Result(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)

    meta_description = models.TextField(max_length=300, blank=True, null=True)
    meta_keywords = models.TextField(max_length=300,blank=True, null=True)

    schema = models.TextField(blank=True, null=True)
    og_image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    og_image_alt = models.CharField(max_length=255,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")
    updated_at = models.DateTimeField(auto_now=True)  # automatic on update


    apply_date = models.CharField(blank=True, null=True)
    vacancy_title = models.TextField(max_length=250, blank=True, null=True) 

    vacancy_name = RichTextField(blank=True, null=True)

    online_application_date= models.CharField(blank=True, null=True)
    online_last_date = models.CharField(max_length=100,blank=True, null=True)
    receipt_of_application = models.CharField(blank=True, null=True)
    last_date_fee = models.CharField(max_length=100,blank=True, null=True)
    correction_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date = models.CharField(max_length=100,blank=True, null=True)
    admit_card_available = models.CharField(max_length=100,blank=True, null=True)
    answerkey_available_date = models.CharField(max_length=100,blank=True, null=True)
    result_available = models.CharField(max_length=100,blank=True, null=True)
    final_result_available = models.CharField(max_length=100,blank=True, null=True)
    
    applecation_fee= RichTextField(blank=True, null=True)

    vacancy_details = RichTextField()
    eligibility_criteria=RichTextField(blank=True, null=True)
    selection_process= RichTextField()

    important_information= RichTextField()
    how_to_apply= RichTextField()

    apply_online_link=models.URLField(blank=True, null=True)
    admitcard_link=models.URLField(blank=True, null=True)
    answerkeyI_link=models.URLField(blank=True, null=True)
    answerkeyII_link=models.URLField(blank=True, null=True)
    result_link=models.URLField(blank=True, null=True)
    resultI_link=models.URLField(blank=True, null=True)
    resultII_link=models.URLField(blank=True, null=True)
    result_final_link=models.URLField(blank=True, null=True)
    notification_link=models.URLField(blank=True, null=True)
    officialwebsite_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("resultpost", kwargs={"slug": self.slug}) 
    
class Meta:
        model = Result
        fields = '__all__'

def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        unique_slug = base_slug
        num = 1
        while Result.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{num}'
        num += 1
        self.slug = unique_slug
    super().save(*args, **kwargs)


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
    title = models.CharField(max_length=100, blank=True, null=True)

    meta_description = models.TextField(max_length=300, blank=True, null=True)
    meta_keywords = models.TextField(max_length=300,blank=True, null=True)

    schema = models.TextField(blank=True, null=True)
    og_image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    og_image_alt = models.CharField(max_length=255,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")
    updated_at = models.DateTimeField(auto_now=True)  # automatic on update


    apply_date = models.CharField(blank=True, null=True)
    vacancy_title = models.TextField(max_length=250, blank=True, null=True) 

    vacancy_name = RichTextField(blank=True, null=True)

    online_application_date= models.CharField(blank=True, null=True)
    online_last_date = models.CharField(max_length=100,blank=True, null=True)
    receipt_of_application = models.CharField(blank=True, null=True)
    last_date_fee = models.CharField(max_length=100,blank=True, null=True)
    correction_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date = models.CharField(max_length=100,blank=True, null=True)
    admit_card_available = models.CharField(max_length=100,blank=True, null=True)
    answerkey_available_date = models.CharField(max_length=100,blank=True, null=True)
    result_available = models.CharField(max_length=100,blank=True, null=True)
    final_result_available = models.CharField(max_length=100,blank=True, null=True)
    
    applecation_fee= RichTextField(blank=True, null=True)

    vacancy_details = RichTextField()
    eligibility_criteria=RichTextField(blank=True, null=True)
    selection_process= RichTextField()

    important_information= RichTextField()
    how_to_apply= RichTextField()

    apply_online_link=models.URLField(blank=True, null=True)
    admitcard_link=models.URLField(blank=True, null=True)
    answerkeyI_link=models.URLField(blank=True, null=True)
    answerkeyII_link=models.URLField(blank=True, null=True)
    result_link=models.URLField(blank=True, null=True)
    resultI_link=models.URLField(blank=True, null=True)
    resultII_link=models.URLField(blank=True, null=True)
    result_final_link=models.URLField(blank=True, null=True)
    notification_link=models.URLField(blank=True, null=True)
    officialwebsite_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("jobpost", kwargs={"slug": self.slug}) 

class Meta:
        model = Job
        fields = '__all__'

def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        unique_slug = base_slug
        num = 1
        while Job.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{num}'
        num += 1
        self.slug = unique_slug
    super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Syllabus(models.Model):
    title = models.CharField(max_length=250)
    admission_date = models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.title