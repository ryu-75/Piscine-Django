from django.utils.translation import gettext_lazy as _
from django.db import models
from ex.models import Users
from django.utils import timezone

class Tip(models.Model):
    content = models.TextField(_('content'))
    date = models.DateTimeField(_('datetime'), default=timezone.now)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    downvoted = models.ManyToManyField(Users, related_name='downvoted', blank=True)
    upvoted = models.ManyToManyField(Users, related_name='upvoted', blank=True)
    
    class Meta:
        db_table = 'tip' 
        
    def get_upvoted_count(self):
        return self.upvoted.count()
    
    def get_downvoted_count(self):
        return self.downvoted.count()
  
    def __str__(self):
        return self.content
    
    def vote(self, user, vote_type):
        if vote_type == 'upvoted':
            if Tip.upvoted.filter(id=user.id).exists():
                Tip.upvoted.remove(user)
            else:
                Tip.upvoted.add(user)
        else: 
            if Tip.downvoted.filter(id=user.id).exists():
                Tip.downvoted.remove(user)
            else:
                Tip.downvoted.add(user)