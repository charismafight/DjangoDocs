# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='mytest',
            field=models.CharField(default='', max_length=10),
        ),
    ]
