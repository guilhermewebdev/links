from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import ListView, DetailView
from . import forms, models
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


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
        if user is not None:
            if user.is_active:
                login(self.request, user)
            else: raise PermissionDenied
        else: raise PermissionDenied
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


class SettingsView(
    CreateView,
    ListView,
    LoginRequiredMixin
):
    template_name = 'settings.html'
    model = models.Store
    form_class = forms.CreateStoreForm
    login_url = '/login/'
    redirect_field_name = 'next'
    context_object_name = 'stores'

    def get_success_url(self):
        if 'store' in dir(self):
            return f'/settings/{self.store}/'
        else: return '/settings/'

    def get_context_data(self, *args, **kwargs):
        self.object_list = self.model.objects.filter(
            owner=self.request.user,
        ).all()
        context = super(SettingsView, self).get_context_data(*args, **kwargs)
        context['stores'] = self.object_list
        
        return context

    def form_valid(self, form):
        store = form.save(commit=False)
        store.owner = self.request.user
        store.save()
        self.store = store.pk
        return super().form_valid(form)

class SetUpStore(
    LoginRequiredMixin,
    UpdateView,
    DetailView,
):
    template_name = 'store_settings.html'
    form_class = forms.SettingsForm
    login_url = '/login/'
    redirect_field_name = 'next'
    model = models.Store
    context_object_name = 'store'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["item_form"] = forms.ItemsForm(self.request.POST)
        else:
            data["item_form"] = forms.ItemsForm()
        return data

    def get_success_url(self):
        if self.kwargs != {}:
            return f'/settings/{self.kwargs.get("pk")}/'
        else: return '/settings/'

    def form_valid(self, form):
        context = self.get_context_data()
        item = context["item_form"]
        self.object = form.save()
        item.instance = self.object
        item.save()
        return super().form_valid(form)

class StoreView(DetailView):
    template_name = 'store.html'
    model = models.Store
    context_object_name = 'store'
    
    def get_object(self, *args, **kwargs):
        return self.model.objects.get(
            slug=self.kwargs.get('store')
        )