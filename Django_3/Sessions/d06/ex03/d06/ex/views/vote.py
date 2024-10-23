from . import View
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from ex.models import Tip

class VoteView(View):
    def post(self, request, tip_id, vote_type):
        tip = get_object_or_404(Tip, id=tip_id)
        
        if request.user.is_authenticated:
            tip.vote(request.user, vote_type)
            messages.info(request, "Your vote are confirmed !")
        else:
            messages.info(request, "Your vote cannot be confirmed...")
        return HttpResponseRedirect('home')
    
