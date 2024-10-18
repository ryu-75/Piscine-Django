from typing import Any
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic.edit import FormView
from ex00.forms.subscriptionForm import SubscriptionForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.urls import reverse

# https://docs.djangoproject.com/fr/5.1/topics/auth/passwords/

@method_decorator(never_cache, name='dispatch')
class Subscription(FormView):
    template_name = 'ex00/form.html'
    form_class = SubscriptionForm
    success_url = '/connexion'
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('/'))
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: str):
        context = super().get_context_data(**kwargs)
        anonymous_session = self.request.session.get('anonymous', 'default')
        context['anonymous'] = anonymous_session
        context['page_title'] = 'Subscription'
        context['get_method'] = 'post'
        return context
    
    def form_valid(self, form):
        form.record_data()
        return super().form_valid(form)