from django.urls import reverse
from django.contrib import messages
from ex.models import UserFavoriteArticle
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, HttpResponseRedirect

class FavouritesView(LoginRequiredMixin, ListView):
    template_name = 'articles/favourites.html'
    model = UserFavoriteArticle
    context_object_name = 'favourites'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if self.request.user.is_authenticated:
            queryset = UserFavoriteArticle.objects.filter(user=user)
            context['favourites'] = list(queryset)
        else:
            context['favourites'] = []
        return context
    
    
    def post(self, request) -> HttpResponse:
        if request.user.is_authenticated:
            article_id = request.POST.get('article_id')
            action = request.POST.get('action')
            success = False
            if article_id:
                if action =='remove':
                    success = UserFavoriteArticle.remove_from_favorite(self, self.request.user, article_id)
                else:
                    messages.warning(request, "Invalid action.")
                messages.success(request, "Valid action") if success else messages.warning(request, "Invalid action.")
            else:
                messages.warning(request, "Invalid article ID.")
            return HttpResponseRedirect(reverse('favourites'))
        else:
            messages.warning(request, "You need to be logged in to add favorites.")
        