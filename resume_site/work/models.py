from django.db import models
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
    website_link = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.company + ' - ' + self.title
