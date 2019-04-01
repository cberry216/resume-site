from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Experience

# Create your views here.


class ExperienceListView(ListView):
    model = Experience
    template_name = 'life/experience_list.html'
    context_object_name = 'experiences'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'life'
        return context


class ExperienceDetailView(DetailView):
    model = Experience
    template_name = 'life/experience_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'life'
        return context


def about_me(request):
    return render(request, 'about.html')
