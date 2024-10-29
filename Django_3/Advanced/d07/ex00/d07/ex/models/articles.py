from django.db import models
from django.utils.translation import gettext_lazy as _
from . import User

class Articles(models.Model):
    title = models.CharField(_("title"), max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    synopsis = models.CharField(_("synopsis"), max_length=312)
    content = models.TextField(_("content"))
    
    class Meta:
        db_table = 'articles'
        
    def __str__(self):
        return self.title