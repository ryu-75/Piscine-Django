from django.http import HttpResponse, HttpRequest
from django.views.generic.base import TemplateView
from typing import Dict, Any
from django.shortcuts import redirect, render


class HomeView(TemplateView):
    template_name = "index.html"

    def get(
        self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect("login")
        return render(request, self.template_name)
