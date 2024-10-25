# Generated by Django 4.2.16 on 2024-10-24 10:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0002_tip_downvoted_tip_upvoted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='downvoted',
            field=models.ManyToManyField(default=0, related_name='downvoted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tip',
            name='upvoted',
            field=models.ManyToManyField(default=0, related_name='upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]
