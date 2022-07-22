from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name="blog"

urlpatterns = [
    path('', views.job, name="homepage"),
    path('skill/', views.skill, name="skillpage"),
    path('<int:pk>', views.candidate, name="candidate"),
]