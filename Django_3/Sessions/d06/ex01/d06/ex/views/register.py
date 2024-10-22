from typing import Any
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic.edit import FormView
from ex.forms.register_form import RegisterForm
from django.urls import reverse

# https://docs.djangoproject.com/fr/5.1/topics/auth/passwords/

class Register(FormView):
    template_name = 'form.html'
    form_class = RegisterForm
    success_url = '/login'
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            messages.error(self.request, "You are already register")
            return HttpResponseRedirect(reverse('home'))
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: str):
        context = super().get_context_data(**kwargs)
        anonymous_session = self.request.session.get('anonymous', 'default')
        context['anonymous'] = anonymous_session
        context['page_title'] = 'Register'
        context['get_method'] = 'post'
        return context
    
    def form_valid(self, form):
        user = form.record_data()
        login(self.request, user)
        messages.info(self.request, "Welcome ! You are now logged in.")
        return HttpResponseRedirect('/')
    
    def form_invalid(self, form):
        messages.error(self.request, "An issue occured during the registration")
        return super().form_invalid(form)