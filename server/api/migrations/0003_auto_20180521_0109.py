# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180521_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='messageSender',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]