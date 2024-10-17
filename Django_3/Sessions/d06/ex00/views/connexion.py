from django.views.generic.edit import FormView
from ex00.forms.connexionForm import ConnexionForm

class Connexion(FormView):
    template_name = 'ex00/form.html'
    form_class = ConnexionForm
    success_url = '/'
    
    def get_context_data(self, **kwargs: str):
        context = super().get_context_data(**kwargs)
        anonymous_session = self.request.session.get('anonymous', 'default')
        context['page_title'] = 'Connexion'
        context['anonymous'] = anonymous_session
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)