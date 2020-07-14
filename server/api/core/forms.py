from django import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Store

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
            'background_image',
            'slug',
            'background_color',
            'rounded',
            'logo',
            'item_size',
            'font',
            'title',
            'description',
            'pixel',
            'analytics',
        )