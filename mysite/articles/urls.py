from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articles, name="posts.html"),
]