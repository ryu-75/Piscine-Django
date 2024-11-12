from typing import Any
from ex.models import Articles
from django.urls import reverse
from django.contrib import messages
from django.views.generic.list import ListView
from django.shortcuts import HttpResponseRedirect

class PublicationsView(ListView):
    template_name = 'articles/publications.html'
    model = Articles
    context_object_name = 'articles'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            queryset = Articles.objects.filter(author=user).values_list('id', flat=True)
            context['publication'] = list(queryset)
        return context 
    
    def post(self, request):
        if request.user.is_authenticated:
            article_id = request.POST.get('article_id')
            print(article_id)
            action = request.POST.get('action')
            success = False
            if article_id:
                if action == 'remove':
                    success = Articles.remove_article(self, self.request.user, article_id)
                    print(success)
                else:
                    messages.warning(request, "Invalid action.")
                messages.success(request, "Valid action") if success else messages.warning(request, "Invalid action.")
            else:
                messages.warning(request, "Invalid article ID.")
            return HttpResponseRedirect(reverse('publication'))