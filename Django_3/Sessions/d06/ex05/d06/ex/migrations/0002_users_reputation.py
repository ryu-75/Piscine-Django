# Generated by Django 4.2.16 on 2024-10-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='reputation',
            field=models.IntegerField(default=0, verbose_name='reputation'),
        ),
    ]
