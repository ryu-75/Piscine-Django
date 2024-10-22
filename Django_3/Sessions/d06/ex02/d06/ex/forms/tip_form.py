from django import forms
from ex.models import Tip
from django.db import IntegrityError

class TipForm(forms.ModelForm):
    content = forms.CharField(label='Share your tip !', widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Writing your tip here !', 'required': True})))
    
    class Meta:
        model = Tip
        fields = ['content']
    
    # Get cleaned data
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def record_data(self, author):
        cleaned_data = self.cleaned_data
        try:
            Tip.objects.create(
                content=cleaned_data.get('content'),
                author=author,
            )
            return True
        except IntegrityError:
            return None
        
        