from django.urls import path, include
from . import views

from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.indem, name="service.html"),
]