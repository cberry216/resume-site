from django.urls import path

from .views import (
    ProjectListView,
    ProjectDetailView,
    project_list_by_tag,
    project_list_by_language,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('tag/<slug:tag_slug>', project_list_by_tag, name='project_list_by_tag'),
    path('lang/<language>', project_list_by_language, name='project_list_by_language'),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
]
