from django.db import models
from django.utils import timezone

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

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
