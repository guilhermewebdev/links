from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import authenticate

class LoginView(FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm

    def get_success_url(self):
        if self.request.user.is_authenticated:
            return self.request.GET.get('next', '/')
        return '/login/'
    
    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(
            email=data.get('email', data.get('username')),
            password=data['password']
        )
        return super().form_valid(form)


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = forms.RegisterForm
    
    def get_success_url(self):
        if self.request.user.is_authenticated:
            return self.request.GET.get('next', '/')
        return '/registration/'

    def form_invalid(self, form):
        print(form.non_field_errors())
        return super().form_invalid(form)

    def form_valid(self, form):
        user = form.save()
        authenticate(
            email=user.email,
            password=user.password,
            username=user.username,
        )
        return super().form_valid(form)
