from typing import Any
from ex.models import Tip
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from ex.forms.tip_form import TipForm
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import get_user_model

Users = get_user_model

class DeleteTipView(View):
    """Delete a tip when the delete button is clicked in view"""
    def post(self, request, id):
        tip = get_object_or_404(Tip, pk=id)
        if request.user.reputation >= 30 or request.user.username == tip.author.username or request.user.is_admin:
            messages.info(request, "Your tip is correctly !")
            if tip.author.reputation > 0:
                print(f'user: {tip.author.username}')
                print(f'reputation: {tip.author.reputation}')
                tip.increment_reputation(0, 'delete')
            tip.delete()
        else:
            messages.error(request, "Your tip cannot be delete...")
        return HttpResponseRedirect(reverse('tip'))

class UpvotedTipView(View):
    """
    Allow to upvoted a tip when the upvote button is clicked in view.
    A downvoted is replace by an upvoted if exist
    """
    def post(self, request, id):
        tip = get_object_or_404(Tip, pk=id)
        
        if request.user.is_authenticated and tip.author.username != request.user.username:
            existing_upvoted = tip.upvoted.filter(author=request.user).first()
            if existing_upvoted:
                tip.upvoted.remove(existing_upvoted)
                messages.info(request, "Downvote was delete!")
            else:
                tip.get_upvoted(request.user)
                messages.info(request, "Upvote confirmed !")
        else:
            messages.error(request, "You can't juged yourself !")
        return HttpResponseRedirect(reverse('tip'))
    
class DownvotedTipView(View):
    """
    Allow to downvoted a tip when the upvote button is clicked in view.
    A upvoted is replace by an downvoted if exist
    """
    def post(self, request, id):
        tip = get_object_or_404(Tip, pk=id)
        
        if request.user.is_authenticated and tip.author.username != request.user.username or request.user.reputation >= 15:
            existing_downvote = tip.downvoted.filter(author=request.user).first()
            if existing_downvote:
                tip.downvoted.remove(existing_downvote)
                messages.info(request, "Downvote was delete!")
            else:
                tip.get_downvoted(request.user)
                messages.info(request, "Downvote confirmed !")
        else:
            messages.error(request, "You can't juged yourself !")
        return HttpResponseRedirect(reverse('tip'))

class TipView(FormView):
    template_name = 'index.html'
    form_class = TipForm
    success_url = reverse_lazy('tip')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['link'] = 'tip'
        context['get_method'] = 'post'
        context['form'] = self.form_class
        context['tips'] = Tip.objects.all().order_by('-date')
        return context
    
    def form_valid(self, form: TipForm) -> HttpResponse:
        if self.request.user.is_authenticated:
            form.record_data(self.request.user)
        messages.info(self.request, "Your tips is shared to everyone !")
        return super().form_valid(form)
    
    def form_invalid(self, form: TipForm) -> HttpResponse:
        messages.error(self.request, "Your tips cannot be share...")
        return super().form_invalid(form)

    