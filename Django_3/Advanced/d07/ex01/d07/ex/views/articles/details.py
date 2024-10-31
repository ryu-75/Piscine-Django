from typing import Any
from ex.models import Articles, UserFavoriteArticle
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

class DetailsView(TemplateView):
    template_name = 'articles/details.html'
    context_object_name = 'liked_articles'  # Renommer pour plus de clarté

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Récupérer tous les articles écrits par l'utilisateur
        authored_articles = Articles.objects.filter(author=user)
        
        # Récupérer tous les articles que l'utilisateur a "likés"
        liked_articles = UserFavoriteArticle.objects.filter(user=user).values_list('article', flat=True)
        
        # Ajouter les articles au contexte
        context['authored_articles'] = authored_articles
        context['liked_articles'] = Articles.objects.filter(id__in=liked_articles)
        
        return context
