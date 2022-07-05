from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import CreateView
# Create your views here.


class SignupView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'
