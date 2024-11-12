from typing import Any, Dict
from django.views.generic.edit import FormView
from ex.forms import LoginForm
from django.contrib.auth import login
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate

class Login(FormView):
    template_name = 'articles.html'
    form_class = LoginForm
    success_url = "/"
    
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            messages.error(self.request, "You're already connected")
            return HttpResponseRedirect(self.success_url)
        return super().get(request)
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['btn_name'] = 'Sign in'
        context['link'] = 'login'
        return context
    
    def form_valid(self, form: LoginForm):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.info(self.request, "You are now logged")
            return HttpResponseRedirect(self.success_url)
        else:
            messages.error(self.request, 'Invalide password and/or username')
            return self.form_invalid(form)
    
    def form_invalid(self, form: LoginForm):
        messages.error(self.request, 'User unfound ! Your information may are not valid')
        return super().form_invalid(form)
    
    