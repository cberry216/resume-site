from django.urls import path

from .views import (
    JobListView,
    JobDetailView,
)

app_name = 'work'

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('job/<slug:slug>', JobDetailView.as_view(), name='job_detail')
]
