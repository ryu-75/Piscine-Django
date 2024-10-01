from django import forms

class Formular(forms.Form):
    firstname = forms.CharField(label="firstname", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Your firstname'}))
    lastname = forms.CharField(label="lastname", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your lastname'}))
    age = forms.IntegerField(label="age", max_value=120, widget=forms.TextInput(attrs={'placeholder': 'Your age'}))
    email = forms.EmailField(label="email", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Your email'}))