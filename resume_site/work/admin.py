from django.contrib import admin

from .models import Job

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'title', 'slug', 'publish')
    search_fields = ('company', 'title', 'description')
    prepopulated_fields = {'slug': ('company', 'title')}
    ordering = ('-publish',)
