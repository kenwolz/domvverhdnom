from django.urls import path
from .views import FeedBackView
from django.conf import settings

urlpatterns = [
    path('', FeedBackView.as_view(), name='feedback_view')
]
