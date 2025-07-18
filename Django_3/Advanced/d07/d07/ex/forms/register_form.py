from django import forms
from ex.models import User
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.Form):
    username = forms.CharField(
        label=_('Username'), 
        max_length=200, 
        widget=forms.TextInput(
            attrs={
                'required': True, 
                'class': 'form-control', 
                'placeholder': _('Username')
            }
    ))
    password = forms.CharField(
        label=_('Password'), 
        max_length=200, 
        widget=forms.PasswordInput(
            attrs={
                'required': True, 
                'class': 'form-control', 
                'placeholder': '*********'
                }
    ))
    repeat_password = forms.CharField(
        label=_('Confirm password'), 
        max_length=200, 
        widget=forms.PasswordInput(
            attrs={
                'required': True, 
                'class': 'form-control', 
                'placeholder': '*********'
                }
    ))
    class Meta:
        model = User
        fields = ['username', 'password', 'repeat_password']
        widget = {
            'password': forms.PasswordInput()
        }
        
    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        rpt_pwd = cleaned_data.get('repeat_password')
        username = cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            return
        if pwd and rpt_pwd and pwd != rpt_pwd:
            raise ValidationError('Password are different...')
        
        return cleaned_data
    
    def record_data(self):
        cleaned_data = self.cleaned_data
        try:
            user = User.objects.create(
                username=cleaned_data.get('username'),
                password=make_password(cleaned_data.get('password'))
            )
            return user
        except IntegrityError:
            return None
        