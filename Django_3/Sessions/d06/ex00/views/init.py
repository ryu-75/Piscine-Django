from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core.cache import cache
from ex00.forms.connexionForm import ConnexionForm
from datetime import datetime

class   Init(View):
    template = 'ex00/init.html'
    def get(self, request):
        anonymous_session = request.session.get('anonymous', 'default')
        context = {'anonymous': anonymous_session}
        return render(request, self.template, context=context)
