from django.contrib import admin

from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    search_fields = ('title', 'short_description', 'long_description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)
