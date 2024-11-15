from django.contrib.auth.views import LogoutView
from typing import Dict, Any
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy

class Logout(LogoutView):
    def get(self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]) -> HttpResponse:
        messages.success(request, 'You have been logged out successfully.')
        return super().get(request, *args, **kwargs)