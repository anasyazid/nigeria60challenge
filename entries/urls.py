from django.urls import path

from .views import ListCreateEntries, EntryDetailView
urlpatterns = [
    path('', ListCreateEntries.as_view()),
    path('<int:id>', ListCreateEntries.as_view()),
]
