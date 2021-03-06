from django.db import models
from django.urls import reverse
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
    updated = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(
        default=0, help_text="Affects how projects show up; lighter projects appear first, heavier projects last.")

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('life:experience_detail', args=[self.slug])
