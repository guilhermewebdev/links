from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms

class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = forms.LoginForm()
        return context