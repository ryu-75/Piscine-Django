from typing import Any
from django.db import models

# Review this model 
class Movies(models.Model):
    # Init models
    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, blank=False, max_length=64)
    director = models.CharField(max_length=32, blank=False)
    producer = models.CharField(max_length=128, blank=False)
    release_date = models.DateField(blank=False)

    class Meta:
        db_table = 'ex05_movies'

    def __str__(self):
        return self.title