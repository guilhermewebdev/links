from django import forms
from django.contrib.auth import get_user_model as usr

class LoginForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = usr()
        fields = (
            'email',
            'password',
        )