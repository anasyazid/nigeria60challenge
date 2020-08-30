from django.urls import path
from django.views.generic import TemplateView

from .views import ListCreateVote, VotingView
urlpatterns = [
    path('', VotingView.as_view(), name='polls'),
    path('vote-submitted/', TemplateView.as_view(template_name='votesuccess.html'), name='vote_success'),
]
