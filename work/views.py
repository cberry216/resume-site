from django.views.generic import ListView, DetailView

from .models import Job

# Create your views here.


class JobListView(ListView):
    model = Job
    template_name = 'work/job_list.html'
    context_object_name = 'jobs'


class JobDetailView(DetailView):
    model = Job
    template_name = 'work/job_detail.html'
