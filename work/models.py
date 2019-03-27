from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Job(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='work/')
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)
    description = models.TextField()
    long_description = models.TextField()
    website_link = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(
        default=0, help_text="Affects how projects show up; lighter projects appear first, heavier projects last.")

    class Meta:
        ordering = ('weight',)

    def __str__(self):
        return self.company + ' - ' + self.title

    def get_absolute_url(self):
        return reverse("work:job_detail", args=[self.slug])
