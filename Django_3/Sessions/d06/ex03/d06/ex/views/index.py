from typing import Any
from django.shortcuts import render
from django.views import View
from ex.models import Tip
from ..forms.tip_form import TipForm

class   Init(View):
    template_name = 'index.html'
    form_class = TipForm
    
    def get(self, request):
        if self.request.user.is_authenticated:
            try:
                tips = Tip.objects.all().order_by('-date')
            except Tip.DoesNotExist as e:
                tips = []
                
            context = {
                'tipsForm': tips,
                'form': self.form_class,
                'tips' : [{
                    'id': tip.id,
                    'author': tip.author,
                    'content': tip.content,
                    'date': tip.date,
                    'upvoted': tip.upvoted,
                    'downvoted': tip.downvoted,
                    'page_title': "Life Pro Tips",
                    'get_method': "post",
                } for tip in tips]
            }
        else:
            context = {'anonymous': self.request.session.get('anonymous', 'default')}
        return render(request, self.template_name, context)