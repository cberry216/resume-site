from django.db import models
from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='projects/')
    short_description = models.TextField()
    long_description = models.TextField()
    language = models.CharField(max_length=40)
    github_link = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(
        default=0, help_text="Affects how projects show up; lighter projects appear first, heavier projects last.")

    tags = TaggableManager()

    class Meta:
        ordering = ('weight',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.slug])
