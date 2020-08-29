from django import forms

from .models import Entry, Person


class EntrySubmissionForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ('person',   )


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'