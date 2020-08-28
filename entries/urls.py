from django.urls import path

from .views import ListCreateEntries, EntryExportView, EntrySubmission
urlpatterns = [
    path('', EntrySubmission.as_view()),
    # path('', ListCreateEntries.as_view()),
    path('export/', EntryExportView.as_view()),
    path('<int:id>', ListCreateEntries.as_view()),
]
