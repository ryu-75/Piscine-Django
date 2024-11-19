from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth import logout
from django.views import View

class Logout(View):
    success_url = '/'
    
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return HttpResponseRedirect(self.success_url)