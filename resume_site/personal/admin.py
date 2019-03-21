from django.contrib import admin

from .models import Experience, Education

# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date_started', 'date_ended', 'publish')
    search_fields = ('name', 'description', 'long_description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-publish')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('college', 'slug', 'date_started', 'date_ended', 'publish')
    search_fields = ('name', 'description', 'long_description')
    prepopulated_fields = {'slug': ('college',)}
    ordering = ('-publish')
