from django.db import models

class Ex03_movies(models.Model):
    # Init models
    title = models.CharField(unique=True, blank=False, max_length=64)
    episode_nb = models.IntegerField(primary_key=True)
    director = models.CharField(max_length=32, blank=False)
    producer = models.CharField(max_length=128, blank=False)
    release_date = models.DateField(blank=False)
    
    class Meta:
        db_table='ex03_movies'
    
    def __str__(self):
        return self.title
    
