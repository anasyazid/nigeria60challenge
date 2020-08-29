from django.urls import path
from django.views.generic import TemplateView

from .views import ListCreateVote
urlpatterns = [
    path('', ListCreateVote.as_view()),
    path('view/', TemplateView.as_view(template_name='vote.html')),
]
