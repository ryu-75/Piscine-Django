# Generated by Django 4.2.16 on 2024-10-23 15:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='downvoted',
            field=models.ManyToManyField(blank=True, related_name='downvoted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tip',
            name='upvoted',
            field=models.ManyToManyField(blank=True, related_name='upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]
