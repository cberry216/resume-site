from django.urls import path

from .views import (
    EducationListView,
    EducationDetailView,
)

app_name = 'education'

urlpatterns = [
    path('', EducationListView.as_view(), name='education_list'),
    path('college/<slug:slug>', EducationListView.as_view(), name='education_detail')
]
