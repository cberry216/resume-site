from django.contrib import admin

from .models import Experience

# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'slug', 'date_started', 'date_ended', 'publish')
    search_fields = ('name', 'description', 'long_description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('weight',)
