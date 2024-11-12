from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.conf import settings
from django.views.generic import FormView
from ex.forms.article_form import ArticleForm
from django.urls import reverse

class PublishView(FormView):
    template_name = 'form.html'
    form_class = ArticleForm
    success_url = 'publication'
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['link'] = 'publish'
        if self.request.LANGUAGE_CODE == 'en':
            context['btn_name'] = 'Share'
            context['page_title'] = 'Do you have an idea ?'
        else:
            context['btn_name'] = 'Partager'
            context['page_title'] = 'Avez-vous une idée ?'
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        user = self.request.user
        form.record_data(user)
        print('Valid form')
        return HttpResponseRedirect(reverse(self.get_success_url()))
    
    def form_invalid(self, form):
        print('Invalid form')
        return super().form_invalid(form)
    