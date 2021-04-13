from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Education(models.Model):
    college = models.CharField(max_length=70)
    abbreviation = models.CharField(max_length=10)
    slug = models.SlugField(max_length=70)
    image = models.ImageField(blank=True, null=True, upload_to='college')
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)
    description = models.TextField()
    long_description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(
        default=0, help_text="Affects how projects show up; lighter projects appear first, heavier projects last.")

    class Meta:
        ordering = ('weight',)

    def __str__(self):
        return self.college

    def get_absolute_url(self):
        return reverse("education:education_detail", args=[self.slug])
