# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-30 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_invisible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(default='Inne', max_length=200),
        ),
    ]
