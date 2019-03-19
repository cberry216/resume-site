from django.views.generic import ListView

from .models import Project

# Create your views here.


class ProjectList(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'project_list'
