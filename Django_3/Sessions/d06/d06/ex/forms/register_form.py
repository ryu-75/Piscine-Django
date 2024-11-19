from django import forms
from django.core.exceptions import ValidationError
from ..models import Users
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={"required": True, "class": 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"required": True, "class": 'form-control', 'placeholder': 'Password'}))
    repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"required": True, "class": 'form-control', 'placeholder': 'Repeat password'}))
    
    class Meta:
        model = Users
        fields = ['username', 'password', 'repeat_password']
        widget = {
            'password': forms.PasswordInput()
        }
    
    # Get cleaned data
    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        rpt_pwd = cleaned_data.get('repeat_password')
        username = cleaned_data.get('username')
        
        
        if Users.objects.filter(username=username).exists():
            return
        if pwd and rpt_pwd and pwd != rpt_pwd:
            raise ValidationError("Password are different")

        return cleaned_data
    
    # recording data
    def record_data(self):
        cleaned_data = self.cleaned_data
        try:
            user = Users.objects.create(
                username=cleaned_data.get('username'),
                password=make_password(cleaned_data.get('password'))
            )
            return user
        except IntegrityError:
            return None