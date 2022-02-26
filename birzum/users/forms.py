from allauth.account.forms import SignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Profile
User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("Ushbu foydalanuvchi nomi band.")}
        }
class UserAddressCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['region', 'district', 'street', 'house', 'postcode', 'phone', ]
        widgets = {
            'region': forms.TextInput(attrs = {'placeholder': 'Viloyat','class': 'form-select form-control'}),
            'district': forms.TextInput(attrs = {'placeholder': 'Shahar', 'class':'form-control'}),
            'street': forms.TextInput(attrs = {'placeholder': 'Ko\'cha nomini kiriting', 'class': 'form-control'}),
            'house': forms.TextInput(attrs = {'placeholder': 'Uy raqamini kiriting', 'class': 'form-control'}),
            'postcode': forms.TextInput(attrs = {'placeholder': 'Pochta raqamini kiriting', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs = {'placeholder': 'Tel: (masalan: 99899 123 45 67)', 'class': 'form-control'}),
        }



class BaseUserSignupForm(SignupForm):

    first_name = forms.CharField(
        max_length=255,
        label=_("Foydalanuvchi ismi"),
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Foydalanuvchi ismi"}))

    last_name = forms.CharField(
        max_length=255,
        label=_("Familiyasi"),
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Familiyasi"}))

    username = forms.CharField(
        max_length=255,
        label=_("Foydalanuvchi nomi"),
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Foydalanuvchi nomi"}))

    email = forms.EmailField(
        max_length=255,
        label=_("Elektron pochta"),
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Elektron pochta"}))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    field_order = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(BaseUserSignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                'autocomplete': 'new-password',
                "placeholder": "********"})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                'autocomplete': 'new-password',
                "placeholder": "********"})

