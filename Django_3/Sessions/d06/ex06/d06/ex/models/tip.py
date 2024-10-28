from django.utils.translation import gettext_lazy as _
from django.db import models
from ex.models import Users

class UpvotedModel(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class DownvoteModel(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Tip(models.Model):
    content = models.TextField(_('content'))
    date = models.DateTimeField(_('datetime'), auto_now_add=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    upvoted = models.ManyToManyField(UpvotedModel)
    downvoted = models.ManyToManyField(DownvoteModel)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tip' 
        permissions = [
            ('auth_delete_tip', 'can delete tip'),
            ('can_add_downvote', 'can add downvote')
        ]
        
        
    def get_upvoted(self, user):
        try:
            downvoted: DownvoteModel = self.downvoted.get(author=user)
            downvoted.delete()
        except DownvoteModel.DoesNotExist:
            pass
        
        if not self.upvoted.filter(author=user).exists():
            upvoted = UpvotedModel(author=user)
            upvoted.save()
            self.upvoted.add(upvoted)
                            
    def get_downvoted(self, user):
        try:
            upvoted: UpvotedModel = self.upvoted.get(author=user)
            upvoted.delete()
        except UpvotedModel.DoesNotExist:
            pass
        
        if not self.downvoted.filter(author=user).exists():
            downvoted = DownvoteModel(author=user)
            downvoted.save()
            self.downvoted.add(downvoted)