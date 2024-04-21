from django.contrib.auth import forms as auth_forms, get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms

from hit_dakwerken.accounts.models import AppUserProfile

UserModel = get_user_model()


class AppUserRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="",
    )
    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="",
    )


class AppUserEditForm(forms.ModelForm):
    class Meta:
        model = AppUserProfile
        fields = ('first_name', 'last_name', 'company_name', 'company_address', 'company_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'company_name': 'Company Name',
            'company_address': 'Company Address',
            'company_url': 'Company URL'
        }
