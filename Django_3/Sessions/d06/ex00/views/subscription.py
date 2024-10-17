from django.views.generic.edit import FormView
from ex00.forms.subscriptionForm import SubscriptionForm

# https://docs.djangoproject.com/fr/5.1/topics/auth/passwords/

class Subscription(FormView):
    template_name = 'ex00/form.html'
    form_class = SubscriptionForm
    success_url = '/connexion/'
    
    def get_context_data(self, **kwargs: str):
        context = super().get_context_data(**kwargs)
        anonymous_session = self.request.session.get('anonymous', 'default')
        context['anonymous'] = anonymous_session
        context['page_title'] = 'Subscription'
        return context
    
    def form_valid(self, form):
        form.record_data()
        return super().form_valid(form)