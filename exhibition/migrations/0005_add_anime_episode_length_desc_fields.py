# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0004_detailed_anime_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='episodes',
            new_name='episode_length',
        ),
        migrations.AddField(
            model_name='anime',
            name='desc',
            field=models.TextField(blank=True, default=b''),
        ),
    ]
