from typing import Any
from ex.models import Articles
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

class   DetailsView(TemplateView):
    template_name = 'details.html'
    model = Articles
    context_object_name = 'details'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        if not pk:
            context['details'] = Articles.objects.all()
        else:
            article = get_object_or_404(Articles, pk=pk)
            context[self.context_object_name] = article
        return context