from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.CharField(max_length=50)
    short_description = models.TextField()
    long_description = models.TextField()
    link_to = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)

    tags = TaggableManager()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
