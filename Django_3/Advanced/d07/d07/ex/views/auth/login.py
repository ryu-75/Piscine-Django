from typing import Any, Dict
from django.views.generic.edit import FormView
from ex.forms import LoginForm
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from ex.models import User
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate

class Login(FormView):
    template_name = 'articles.html'
    form_class = LoginForm
    success_url = "/"
    
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            messages.error(self.request, "You're already connected")
            return HttpResponseRedirect(self.success_url)
        return super().get(request)
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['btn_name'] = 'Sign in'
        context['link'] = 'login'
        return context
    
    def form_valid(self, form: LoginForm) -> HttpResponse:
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.warning(self.request, "Username not found.")
            return HttpResponseRedirect(self.success_url)
        
        user = authenticate(self.request, username=username, password=password)
        
        if user is None:
            messages.warning(self.request, "Username and/or password are required.")
            return HttpResponseRedirect(self.success_url)
        messages.info(self.request, 'Your connected now !')
        login(self.request, user)
        return super().form_valid(form)

    
    def form_invalid(self, form: LoginForm) -> HttpResponse:
        messages.error(self.request, 'User unfound ! Your information may are not valid')
        return super().form_invalid(form)
    
    