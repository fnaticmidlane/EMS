from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import ParticipantCreationForm

class SignUpView(CreateView):
    form_class = ParticipantCreationForm
    success_url= reverse_lazy ("home")
    template_name = "signup.html"