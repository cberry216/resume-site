from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from taggit.models import Tag

from .models import Project

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'project_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'projects'
        return context


def project_list_by_tag(request, tag_slug=None):
    object_list = Project.objects.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    return render(request, 'projects/project_list.html', {
        'project_list': object_list,
        'tag': tag,
        'section': 'projects'
    })


def project_list_by_language(request, language=None):
    object_list = Project.objects.all()

    lang = None
    if language:
        lang = language
        object_list = object_list.filter(language=language)

    return render(request, 'projects/project_list.html', {
        'project_list': object_list,
        'lang': lang,
        'section': 'projects'
    })


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'projects'
        return context
