from typing import Any, Dict
from django.views.generic.edit import FormView
from ex.forms import LoginForm
from django.contrib.auth import login
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

class Login(FormView):
    template_name = 'articles/articles.html'
    form_class = LoginForm
    success_url = reverse_lazy("home")
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['btn_name'] = 'Sign in'
        context['link'] = 'login'
        return context
    
    def form_valid(self, form: LoginForm) -> HttpResponse:
        user = form.record_data()
        messages.add_message(self.request, messages.INFO, _("You're connected now!"), extra_tags='persistent')
        login(self.request, user)
        return super().form_valid(form)
    
    def form_invalid(self, form: LoginForm) -> HttpResponse:
        messages.add_message(self.request, messages.ERROR, _("User unfound ! Your information may are not valid"), extra_tags='persistent')
        return HttpResponseRedirect(self.success_url)
    
    