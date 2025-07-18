from django import forms
from account.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Enter your username',
        max_length=255,
        widget=forms.TextInput(attrs={
            'required': True,
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        label='Enter your password',
        widget=forms.PasswordInput(attrs={
            'required': True,
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        errors = {}
        
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                errors['password'] = 'Invalid password'
        except User.DoesNotExist:
            errors['username'] = 'Invalid username'
        if errors:
            raise forms.ValidationError(errors)
        return cleaned_data