from django.core.mail import send_mail
from django.db import transaction
from django.views.generic import ListView, FormView, View
from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .forms import EntrySubmissionForm
from .models import Entry
from .serializers import EntrySerializer

from entries.forms import EntrySubmissionForm, PersonCreationForm


class EntrySubmission(View):
    model = Entry
    template_name = 'apply.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'apply.html')

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        entry_form = EntrySubmissionForm(request.POST, request.FILES)
        person_form = PersonCreationForm(request.POST, request.FILES)

        if person_form.is_valid() and entry_form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            person = person_form.save()
            entry = entry_form.save(commit=False)
            entry.person = person
            entry.save()
            send_mail(
                'Application entry received',
                'Thank you for submitting your entry to participate in the Nigeria at 60 challenge. Your entry has '
                'been received, and if shortlisted, you would be contacted for further directiton.',
                'amustapha@hooli.ng',
                [person.email],
                fail_silently=False,
            )

            return render(request, 'entrysuccess.html', {'message': 'Your entry has been successfully submitted.'})
        return render(request, 'apply.html', {'entry_form': entry_form, 'person_form': person_form})


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
