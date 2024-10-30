from django.shortcuts import redirect
from django.views.generic.list import ListView
from ex.models import Articles

class HomeView(ListView):
    template_name = 'articles.html'
    model = Articles
    context_object_name = 'article'
    
    def get(self, request):
        return redirect(self.context_object_name)

