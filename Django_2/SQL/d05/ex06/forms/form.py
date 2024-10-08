from django import forms

class Form(forms.Form):
    title = forms.ChoiceField(choices=(), required=True)
    your_text = forms.CharField(max_length=100, required=True)
    
    def __init__(self, choices, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['title'].choices = choices