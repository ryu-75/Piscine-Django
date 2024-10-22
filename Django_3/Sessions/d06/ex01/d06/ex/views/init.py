from django.shortcuts import render
from django.views import View

class   Init(View):
    template = 'init.html'
    def get(self, request):
        anonymous_session = request.session.get('anonymous', 'default')
        context = {'anonymous': anonymous_session}
        return render(request, self.template, context=context)
