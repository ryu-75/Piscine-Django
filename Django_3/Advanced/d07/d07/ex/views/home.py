from ex.models import Articles
from django.shortcuts import redirect
from django.views.generic.list import ListView

class HomeView(ListView):
    template_name = 'articles/articles.html'
    model = Articles
    context_object_name = 'articles'
    
    def get(self, request):
        return redirect(self.context_object_name)

