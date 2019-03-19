from django.urls import path

from .views import ProjectList

app_name = 'blog'

urlpatterns = [
    path('', ProjectList.as_view(), name='project_list')
]
