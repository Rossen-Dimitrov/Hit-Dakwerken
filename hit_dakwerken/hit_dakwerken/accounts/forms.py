from django.contrib.auth import forms as auth_forms, get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, get_user_model, password_validation
from django import forms

UserModel = get_user_model()


class AppUserRegisterForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()
    username = forms.CharField(
        label=_("Username"),
        strip=False,
        help_text=_(""),
    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=_(""),
    )
    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="",
    )

    # class Mata(auth_forms.UserCreationForm.Meta):
    #     model = UserModel
    #     fields = ('email',)
