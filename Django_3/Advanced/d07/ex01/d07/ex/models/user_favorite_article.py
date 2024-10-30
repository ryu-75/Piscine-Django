from django.db import models
from . import User, Articles

class UserFavoriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'user_favorite_article'
        
    def __str__(self):
        return self.article.title