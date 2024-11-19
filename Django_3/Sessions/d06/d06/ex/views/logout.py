from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.http import HttpRequest, HttpResponse

class Logout(View):
    template = '/'
    
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect(self.template)