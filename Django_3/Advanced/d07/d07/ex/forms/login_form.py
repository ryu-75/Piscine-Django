from django import forms
from django.utils.translation import gettext_lazy as _
from ex.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    username = forms.CharField(
        label="",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "required": True,
                "class": "form-control",
                "id": "username",
                "placeholder": _("Username"),
            }
        ),
    )
    password = forms.CharField(
        label="",
        max_length=200,
        widget=forms.PasswordInput(
            attrs={
                "required": True,
                "class": "form-control",
                "id": "password",
                "placeholder": "*********",
            }
        ),
    )

    def clean(self):
        """
        Check if user exist in database
        """
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            if not user and self.request and self.request.LANGUAGE_CODE == "fr":
                raise ValidationError(_("Informations invalides"))
            else:
                raise ValidationError(_("Invalid information"))
        self.user = user
        return cleaned_data
