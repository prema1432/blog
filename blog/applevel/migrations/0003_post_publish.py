# Generated by Django 2.2 on 2020-02-18 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applevel', '0002_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
