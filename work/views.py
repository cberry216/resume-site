from django.views.generic import ListView, DetailView

from .models import Job

# Create your views here.


class JobListView(ListView):
    model = Job
    template_name = 'work/job_list.html'
    context_object_name = 'jobs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'work'
        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'work/job_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'work'
        return context
