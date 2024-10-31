from typing import Any
from django.views.generic.edit import FormView
from ex.forms import LoginForm
from django.contrib.auth import login
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate

class Login(FormView):
    template_name = 'form.html'
    form_class = LoginForm
    success_url = "/"
    
    def get(self, request):
        if request.user.is_authenticated:
            messages.error(self.request, "You're already connected")
            return HttpResponseRedirect(reverse('home'))
        return super().get(request)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['btn_name'] = "Sign in"
        context['link'] = 'login'
        return context
    
    def form_valid(self, form: LoginForm):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        try:
            user = authenticate(self.request, username=username, password=password)
            messages.info(self.request, "You are now logged")
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        except user.DoesNotExist:
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'User unfound ! Your information may are not valid')
        return super().form_invalid(form)
    
    