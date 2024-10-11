from django.db import models

class Ex03_movies(models.Model):
    # Init models
    title = models.CharField(unique=True, null=False, max_length=64)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    
    class Meta:
        db_table='ex03_movies'
    
    def __str__(self):
        return self.title
    
