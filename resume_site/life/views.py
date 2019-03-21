from django.views.generic import ListView, DetailView

from .models import Experience

# Create your views here.


class ExperienceListView(ListView):
    model = Experience
    template_name = 'life/experience_list.html'
    context_object_name = 'experiences'


class ExperienceDetailView(DetailView):
    model = Experience
    template_name = 'life/experience_detail.html'
