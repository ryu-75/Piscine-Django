# Generated by Django 5.1.1 on 2024-10-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('episode_nb', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
            options={
                'db_table': 'ex05_movies',
            },
        ),
    ]
