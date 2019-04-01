from django.views.generic import ListView, DetailView

from .models import Education

# Create your views here.


class EducationListView(ListView):
    model = Education
    template_name = 'education/education_list.html'
    context_object_name = 'colleges'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'education'
        return context


class EducationDetailView(DetailView):
    model = Education
    template_name = 'education/education_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'education'
        return context
