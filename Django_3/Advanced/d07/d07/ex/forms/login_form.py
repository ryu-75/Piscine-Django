from typing import Any
from django import forms
from django.utils.translation import gettext_lazy as _
from ex.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={
        'required': True, 
        'class': 'form-control',
        'id': 'username',
        'placeholder': _('Username')
    }))
    password = forms.CharField(label='', max_length=200, widget=forms.PasswordInput(attrs={
        'required': True, 
        'class': 'form-control', 
        'id': 'password',
        'placeholder': '*********'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'password']
        widget = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        
        if not user:
            raise ValidationError('Username and/or password invalid')
        return cleaned_data
    
    def record_data(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user