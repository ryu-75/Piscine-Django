from django import forms
from ex00.models.users import Users
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password  
from django.contrib.auth import authenticate, login


class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True})))
    password = forms.CharField(max_length=50, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True})))
    
    class Meta:
        model = Users
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