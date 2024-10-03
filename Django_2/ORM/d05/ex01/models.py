from typing import Any
from django.db import models

# Review this model 
class movies_table(models.Model):
    class movies_text_model(models.TextChoices):
        DIRECTOR = "Greg Araki",
        TITLE = "Kaboum!",
        PRODUCER = "Steven Spieldberg",
        EPISODE_NB = 0
    # Init models
    title = models.CharField(unique=True, blank=False, max_length=64, default=movies_text_model.TITLE)
    episode_nb = models.IntegerField(primary_key=True, default=movies_text_model.EPISODE_NB)
    opening_crawl = models.TextField(blank=True)
    director = models.CharField(max_length=32, blank=False, default=movies_text_model.DIRECTOR)
    producer = models.CharField(max_length=128, blank=False, default=movies_text_model.PRODUCER)
    release_date = models.DateField(blank=False)

        