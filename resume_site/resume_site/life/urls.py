from django.urls import path

from .views import (
    ExperienceListView,
    ExperienceDetailView,
    about_me,
)

app_name = 'life'

urlpatterns = [
    path('', ExperienceListView.as_view(), name='experience_list'),
    path('experience/<slug:slug>', ExperienceDetailView.as_view(), name='experience_detail'),
    # path('about/', about_me, name='about'),
]
