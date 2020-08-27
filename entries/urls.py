from django.urls import path

from .views import ListCreateEntries, EntryExportView
urlpatterns = [
    path('', ListCreateEntries.as_view()),
    path('export/', EntryExportView.as_view()),
    path('<int:id>', ListCreateEntries.as_view()),
]
