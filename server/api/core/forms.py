from django import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Store, Item
from django.forms.models import inlineformset_factory

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
            'title',
            'slug',
        )

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
            'slug',
            'logo',
            'title',
            'description',
            'pixel',
            'analytics',
            'theme',
        )

ThemeForm = inlineformset_factory(
    Store,
    StoreTheme,
    form=SettingsForm,
    extra=1,
    fields=(
        'rounded',
        'item_size',
        'image_position',
        'padding',
        'border_color',
        'border_size',
        'border_style',
        'background_header',
        'logo_position',
        'background_image',
    )
)

ItemsForm = inlineformset_factory(
    Store,
    Item,
    form=SettingsForm,
    extra=1,
    can_order=True,
    fields=(
        'title',
        'description',
        'price',
        'link',
        'image',
        'reference',
        'index',
    )
)    