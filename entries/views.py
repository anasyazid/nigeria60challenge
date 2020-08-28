from django.views.generic import ListView, FormView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .forms import EntrySubmissionForm
from .models import Entry
from .serializers import EntrySerializer


class EntrySubmission(FormView):
    model = Entry
    form_class = EntrySubmissionForm
    template_name = 'apply.html'


class ListCreateEntries(ListCreateAPIView):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
    permission_classes = []

    def get(self, request, *args, **kwargs):
        # if request.user.is_anonymous:
        #     return JsonResponse({"status": False, "message": "Login required to see entries"}, status=401)
        # if not request.user.is_staff:
        #     return JsonResponse({"status": False, "message": "Staff login required to see entries"}, status=403)
        return super(ListCreateEntries, self).get(request, *args, **kwargs)


class EntryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()


class EntryExportView(ListView):
    model = Entry
    queryset = Entry.objects.all()
    template_name = 'export.html'
