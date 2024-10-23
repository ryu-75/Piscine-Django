from typing import Any
from django.views.generic.edit import FormView
from ex.forms.login_form import ConnexionForm
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

class Login(FormView):
    template_name = 'form.html'
    form_class = ConnexionForm
    success_url = '/'
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            messages.error(self.request, "You are already logged in !")
            return HttpResponseRedirect(reverse('home'))
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: str):
        context = super().get_context_data(**kwargs)
        anonymous_session = self.request.session.get('anonymous', 'default')
        context['page_title'] = 'Log in'
        context['get_method'] = 'post'
        context['anonymous'] = anonymous_session
        return context
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        
        if user is None:
            messages.error(self.request, "Username and/or password are required")
            return self.form_invalid(form)
        messages.info(self.request, "You're connected now !")
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return super().form_invalid(form)