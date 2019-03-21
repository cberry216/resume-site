from django.db import models
from django.utils import timezone

# Create your models here.


class Experience(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='life/')
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)
    description = models.TextField()
    long_description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name


class Education(models.Model):
    college = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    image = models.ImageField(blank=True, null=True, upload_to='college')
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)
    description = models.TextField()
    long_description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.college