from django.db import models
from django.utils.translation import gettext_lazy as _
from . import User
from django.core.exceptions import ValidationError

class Articles(models.Model):
    title = models.CharField(_("title"), max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    synopsis = models.CharField(_("synopsis"), max_length=312)
    content = models.TextField(_("content"))
    
    class Meta:
        db_table = 'articles'
        
    def remove_article(self, user, article_id):
        """
        Remove an article from the user's articles
        """
        remove = False
        try:
            remove = Articles.objects.filter(author=user, id=article_id)
            print(remove)
            if remove.exists():
                remove.delete()
                print("Article was correctly deleted")
            else:
                print('This article is not in your favorites')
        except Exception as e:
            raise ValidationError(f"Error: {e}")
        
    def __str__(self):
        return self.title
    
class UserFavoriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'user_favorite_article'
        unique_together = ('user', 'article')
        
    def add_to_favorite_article(self, user, article_id):
        """
        Adds an article to the user's favorites
        """
        created = False
        try:
            created = UserFavoriteArticle.objects.get_or_create(user=user, article_id=article_id)
            if created:
                print("Article was correctly added")
            else:
                raise ValidationError("This article is already in your favorites")
            return created
        except Exception as e:
            raise ValidationError(f"Error: {e}")
        
    def remove_from_favorite(self, user, article_id):
        """
        Remove an article from the user's favorites
        """
        remove = False
        try:
            remove = UserFavoriteArticle.objects.filter(user=user, article_id=article_id)
            if remove.exists():
                remove.delete()
                print("Article was correctly deleted")
            else:
                print('This article is not in your favorites')
            return remove
        except Exception as e:
            raise ValidationError(f"Error: {e}")
    
    def __str__(self):
        return self.article.title