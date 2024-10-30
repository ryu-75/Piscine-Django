from typing import Any
from ex.models import Articles
from django.views.generic.list import ListView

class PublicationsView(ListView):
    template_name = 'publications.html'
    model = Articles
    context_object_name = 'publications'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context 