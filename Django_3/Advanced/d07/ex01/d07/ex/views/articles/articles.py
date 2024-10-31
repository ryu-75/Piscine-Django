from typing import Any
from django.urls import reverse
from django.contrib import messages
from django.views.generic.list import ListView
from ex.models import Articles, UserFavoriteArticle
from django.shortcuts import HttpResponse, HttpResponseRedirect

class ArticlesView(ListView):
    template_name = 'articles/articles.html'
    model = Articles
    context_object_name = 'articles'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            queryset = UserFavoriteArticle.objects.filter(user=user).values_list('article_id', flat=True)
            context['favorites'] = list(queryset)
        else:
            context['favorites'] = []
        return context    
    
    def post(self, request) -> HttpResponse:
        if request.user.is_authenticated:
            article_id = request.POST.get('article_id')
            action = request.POST.get('action')
            success = False
            
            if article_id:
                if action == 'add':
                    success = UserFavoriteArticle.add_to_favorite_article(self, self.request.user, article_id)
                elif action =='remove':
                    success = UserFavoriteArticle.remove_from_favorite(self, self.request.user, article_id)
                else:
                    messages.warning(request, "Invalid action.")
                messages.success(request, "Valid action") if success else messages.warning(request, "Invalid action.")
            else:
                messages.warning(request, "Invalid article ID.")
            return HttpResponseRedirect(reverse('article'))
        else:
            messages.warning(request, "You need to be logged in to add favorites.")
        