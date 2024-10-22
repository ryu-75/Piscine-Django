from django.utils.translation import gettext_lazy as _
from django.db import models
from ex.models import Users
from django.utils import timezone

class Tip(models.Model):
    content = models.TextField(_('content'))
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(_('datetime'), default=timezone.now)
    
    class Meta:
        db_table = 'tip'
    
    def __str__(self):
        return self.content