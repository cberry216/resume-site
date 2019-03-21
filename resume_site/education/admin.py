from django.contrib import admin

from .models import Education
# Register your models here.


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('college', 'slug', 'date_started', 'date_ended', 'publish')
    search_fields = ('name', 'description', 'long_description')
    prepopulated_fields = {'slug': ('college',)}
    ordering = ('-publish',)
