from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout
from django.views import View

class Logout(View):
    success_url = '/'
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(self.success_url)