from django import forms
from ex00.models.users import Users

class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True})))
    password = forms.CharField(max_length=50, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True})))
    
    class Meta:
        model = Users
        fields = ['username', 'password']
        widget = {
            'password': forms.PasswordInput()
        }
    