from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import authenticate

class LoginView(FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.request.GET.get('next', '/'))
        return super().get(*args, **kwargs)

    def get_success_url(self):
        return self.request.GET.get('next', '/')
    
    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        user = authenticate(
            username=data.get('email', data.get('username')),
            password=data['password']
        )
        print(user)
        return super().form_valid(form)


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = forms.RegisterForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.request.GET.get('next', '/'))
        return super().get(*args, **kwargs)
    
    def get_success_url(self):
        if self.request.user.is_authenticated:
            return self.request.GET.get('next', '/')
        return '/registration/'

    def form_valid(self, form):
        user = form.save()
        authenticate(
            email=user.email,
            password=user.password,
            username=user.username,
        )
        return super().form_valid(form)
