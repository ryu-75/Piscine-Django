from django import forms
from ex.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=200, widget=forms.TextInput(attrs={
        'required': True, 
        'class': 'form-control', 
        'placeholder': 'username'
    }))
    password = forms.CharField(label='password', max_length=200, widget=forms.PasswordInput(attrs={
        'required': True, 
        'class': 'form-control', 
        'placeholder': '*********'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'password']
        widget = {
            'password': forms.PasswordInput()
        }
        
    def clean(self):
        """
        Check if user exist in database
        """
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        
        if not user:
            raise ValidationError('Invalid information')
        return cleaned_data