from django.db import models

class   Movies(models.Model):
    # Init models
    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, null=False, max_length=64)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'ex07_movies'

    def __str__(self):
        return self.title