from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import render
from ex.models import Articles

class ArticlesView(ListView):
    template_name = 'articles.html'
    model = Articles
    context_object_name = 'articles'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context    