from . import View
from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ex.models import Tip

class Tip(View):
    template_name = 'tip.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['author'] = self.request.user.username
            context['tips'] = Tip.objects.all()
        return context
    
    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)