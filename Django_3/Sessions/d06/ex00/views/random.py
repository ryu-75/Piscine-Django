from django.shortcuts import render
from django.views import View
import random 
from django.conf import settings
from django.core.cache import cache
from datetime import datetime

class   Random(View):
    template = 'ex00/init.html'
    def get(self, request):
        timer = datetime.now().second
        context = {'name': request.session.get('name')}
        return render(request, self.template, context=context)
