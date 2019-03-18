from django.db import models
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.CharField(max_length=50)
    short_description = models.TextField()
    long_description = models.TextField()
    link_to = models.CharField(max_length=200)

    class Meta:
        ordering = ('title')

    def __str__(self):
        return self.title
