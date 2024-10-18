from typing import Any
from django.views.generic.edit import FormView
from ex00.forms.connexionForm import ConnexionForm
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.urls import reverse

@method_decorator(never_cache, name='dispatch')
class Login(FormView):
    template_name = 'ex00/form.html'
    form_class = ConnexionForm
    success_url = '/'
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse(''))
        return super().dispatch(request, *args, **kwargs)
    
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
        
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(self.get_success_url())
            else:
                form.add_error(None, "An error is occured.")
                return self.form_invalid(form)
        else:
            form.add_error(None, "Invalid username and/or password")
            return self.form_invalid(form)