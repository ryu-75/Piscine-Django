from django.shortcuts import render
from django.views import View

class   Random(View):
    template = 'ex00/base.html'
    def get(self, request):
        return render(request, self.template)