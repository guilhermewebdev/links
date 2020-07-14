from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from . import forms
from django.contrib.auth import authenticate

class LoginView(TemplateView, FormView):
    template_name = 'login.html'

    def get_form(self, *args, **kwargs):
        return forms.LoginForm()
    
    def post(self, *args, **kwargs):
        user = authenticate(
            email=self.request.POST['email'],
            password=self.request.POST['password']
        )
        if user is not None:
            if 'next' in self.request.GET:
                return redirect(self.request.GET['next'])
            return redirect('/')
        else:
            return redirect('/login/')
