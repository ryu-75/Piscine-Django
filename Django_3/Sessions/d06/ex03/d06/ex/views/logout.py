from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class Logout(View):
    template = '/'
    
    def get(self, request):
        logout(request)
        return redirect(self.template)