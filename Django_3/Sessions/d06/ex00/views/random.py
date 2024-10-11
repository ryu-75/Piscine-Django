from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from random import choice
from django.conf import settings

class   Random(View):
    template = 'ex00/base.html'
    def get(self, request):
        names = request.session.get(settings.USERNAME)
        return render(request, self.template, {'names':choice(names)})