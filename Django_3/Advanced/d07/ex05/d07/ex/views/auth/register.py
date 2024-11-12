from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import FormView
from ex.forms.register_form import RegisterForm
from django.contrib.auth import login
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

class RegisterView(FormView):
    template_name = 'form.html'
    form_class = RegisterForm
    success_url = "/"
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]) -> HttpResponse:
        if request.user.is_authenticated:
            messages.error(self.request, "You are already register !")
            return HttpResponseRedirect(reverse('home'))
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['link'] = 'register'
        if self.request.LANGUAGE_CODE == 'en':
            context['btn_name'] = 'Sign up'
            context['page_title'] = 'Register'
        else:
            context['btn_name'] = "S'inscrire"
            context['page_title'] = 'Inscription'
        return context
    
    def form_valid(self, form: RegisterForm) -> HttpResponse:
        user = form.record_data()
        login(self.request, user)
        messages.info(self.request, "You're correctly registered !")
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form: RegisterForm) -> HttpResponse:
        messages.error(self.request, "Your information are not valid !")
        return super().form_invalid(form)
    