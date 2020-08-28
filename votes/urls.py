from django.urls import path

from .views import ListCreateVote
urlpatterns = [
    path('', ListCreateVote.as_view()),
]
