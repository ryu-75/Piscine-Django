from django import forms
from account.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Enter your username",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "id": "username",
                "required": True,
                "class": "form-control",
                "placeholder": "Username",
            }
        ),
    )
    password = forms.CharField(
        label="Enter your password",
        widget=forms.PasswordInput(
            attrs={
                "id": "password",
                "required": True,
                "class": "form-control",
                "placeholder": "Password",
            }
        ),
    )
    repeat_password = forms.CharField(
        label="Repeat your password",
        widget=forms.PasswordInput(
            attrs={
                "required": True,
                "class": "form-control",
                "placeholder": "Repeat password",
            }
        ),
    )
    image = forms.ImageField(label="Add a profile picture", required=False)

    class Meta:
        model = User
        fields = ["username", "password", "repeat_password", "image"]

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")
        print(repeat_password)

        if User.objects.filter(username=username, password=password).exists():
            raise ValidationError("Username already exists.")
        if password != repeat_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

    def record_data(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get("username"),
            password=self.cleaned_data.get("password"),
            image=self.cleaned_data.get("image"),
        )
        user.save()
        return user
