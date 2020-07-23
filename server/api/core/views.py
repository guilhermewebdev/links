from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import ListView, DetailView
from . import forms, models
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = forms.RegisterForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().get(*args, **kwargs)
    
    def get_success_url(self):
        if self.request.user.is_authenticated:
            return self.request.GET.get('next', '/admin/')
        return '/admin/register/'

    def form_valid(self, form):
        user = form.save()
        auth = authenticate(
            email=user.email,
            password=user.password,
            username=user.username,
        )
        if auth is not None:
            if auth.is_active:
                login(self.request, auth)
            else: raise PermissionDenied
        else: raise PermissionDenied
        return super().form_valid(form)

class StoreView(DetailView):
    template_name = 'store.html'
    model = models.Store
    context_object_name = 'store'

    def get_object(self, *args, **kwargs):
        return self.model.objects.get(
            slug=self.kwargs.get('store')
        )