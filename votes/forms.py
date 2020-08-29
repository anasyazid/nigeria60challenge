from django import forms

from .models import Vote


class VotingForm(forms.ModelForm):
    class Meta:
        model  = Vote
        fields ="__all__"