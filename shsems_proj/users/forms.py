from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Participant

class ParticipantCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Participant
        fields = ('username', 'email', 'last_name', 'contact_number')