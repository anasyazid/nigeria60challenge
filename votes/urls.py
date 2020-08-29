from django.urls import path
from django.views.generic import TemplateView

from .views import ListCreateVote, VotingView
urlpatterns = [
    path('', ListCreateVote.as_view()),
    path('view/', VotingView.as_view()),
]
