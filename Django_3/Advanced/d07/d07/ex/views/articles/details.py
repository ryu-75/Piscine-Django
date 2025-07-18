from typing import Any
from ex.models import Articles, UserFavoriteArticle
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView

class DetailsView(DetailView):
    template_name = 'articles/details.html'
    model = Articles

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        article = context['object']
        context['details'] = UserFavoriteArticle(article_id=article.id)
        return context
