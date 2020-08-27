from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Entry
from .serializers import EntrySerializer


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
    template_name = 'index.html'

