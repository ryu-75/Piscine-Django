# Generated by Django 4.2.16 on 2024-10-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0004_tip_updated_at_alter_tip_date_upvotedmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
