from django.urls import path
from django.views.generic import TemplateView

from .views import ListCreateEntries, EntryExportView, EntrySubmission
urlpatterns = [
    path('', EntrySubmission.as_view(), name='entry_submission'),
    path('guide/', TemplateView.as_view(template_name='guide.html'), name='entries_guide'),
    path('entry-submitted/', TemplateView.as_view(template_name='entrysuccess.html'), name='entries_success'),
    # path('', ListCreateEntries.as_view()),
    path('export/', EntryExportView.as_view()),
    path('<int:id>', ListCreateEntries.as_view()),
]
