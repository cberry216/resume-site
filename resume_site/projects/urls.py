from django.urls import path

from .views import ProjectListView, ProjectDetailView, project_list_by_tag

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('tag/<slug:tag_slug>', project_list_by_tag, name='project_list_by_tag'),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
]
