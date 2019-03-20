from django.views.generic import ListView, DetailView

from .models import Job

# Create your views here.


class JobListView(ListView):
    model = Job
    template_name = 'work/work_list.html'
    context_object_name = 'jobs'
