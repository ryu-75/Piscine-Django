from django import forms

# Define dynamicaly the options form a field selection as ChoiceField during the creation form
class   RemoveForm(forms.Form):
    title = forms.ChoiceField(choices=(), required=True)
    
    def __init__(self, choices, *args, **kwargs):
        super(RemoveForm, self).__init__(*args, **kwargs)   # Init the parent class before process to specific personalisation
        self.fields['title'].choices = choices              # Used for push the options from a field of ChoiceField or Select type