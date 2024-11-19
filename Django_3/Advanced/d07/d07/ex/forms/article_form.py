from django import forms
from ex.models import Articles, User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class ArticleForm(forms.Form):
    title = forms.CharField(
        label=_('Title'), 
        max_length=200, 
        widget=forms.TextInput(attrs={
        'required': True,
        'class': 'form-control',
        'placeholder': _('Article title')
    }))
    synopsis = forms.CharField(
        label='Synopsis', 
        widget=forms.TextInput(attrs={
        'required': False,
        'class': 'form-control',
        'placeholder': _('Article synopsis')
    }))
    content = forms.CharField(
        label=_('Content'), 
        widget=forms.TextInput(attrs={
        'required': True,
        'class': 'form-control',
        'placeholder': _('Article content')
    }))
    
    class Meta:
        model = Articles
        fields = ['title', 'synopsis', 'content']
        
    def record_data(self, user):
        cleaned_data = super().clean()
        try:
            article = Articles.objects.create(
                title = cleaned_data.get('title'),
                synopsis = cleaned_data.get('synopsis'),
                content = cleaned_data.get('content'),
                author_id = user.id
            )
            return article
        except:
            raise ValidationError('You need to be authenticated to share an article')