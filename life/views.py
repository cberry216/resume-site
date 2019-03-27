from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Experience

# Create your views here.


class ExperienceListView(ListView):
    model = Experience
    template_name = 'life/experience_list.html'
    context_object_name = 'experiences'


class ExperienceDetailView(DetailView):
    model = Experience
    template_name = 'life/experience_detail.html'


def about_me(request):
    return render(request, 'about.html')
