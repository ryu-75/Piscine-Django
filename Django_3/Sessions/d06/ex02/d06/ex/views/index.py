from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from ex.forms.tip_form import TipForm
from django.views.generic.edit import FormView
from django.contrib import messages
from ex.models import Tip

class   Init(FormView):
    template_name = 'form.html'
    form_class = TipForm
    success_url = '/'
    
    def get_template_names(self) -> list[str]:
        if self.request.user.is_authenticated:
            return [self.template_name]
        else:
            return ['index.html']
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['form'] = self.form_class()
            context['page_title'] = "Life Pro Tips"
            context['get_method'] =  "post"
            context['author'] = self.request.user.username
            context['tips'] = Tip.objects.all().order_by('-date')
        else:
            context['anonymous'] = self.request.session.get('anonymous', 'default')
        return context
    
    def form_valid(self, form: TipForm) -> HttpResponse:
        if self.request.user.is_authenticated:
            form.record_data(self.request.user)
        messages.info(self.request, "Your tips is shared to everyone !")
        return super().form_valid(form)
    
    def form_invalid(self, form: TipForm) -> HttpResponse:
        messages.error(self.request, "Your tips cannot be share...")
        return super().form_invalid(form)
    
