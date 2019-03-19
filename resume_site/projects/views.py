from django.views.generic import ListView, DetailView

from .models import Project

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'project_list'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
