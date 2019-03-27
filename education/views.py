from django.views.generic import ListView, DetailView

from .models import Education

# Create your views here.


class EducationListView(ListView):
    model = Education
    template_name = 'education/education_list.html'
    context_object_name = 'colleges'


class EducationDetailView(DetailView):
    model = Education
    template_name = 'education/education_detail.html'
