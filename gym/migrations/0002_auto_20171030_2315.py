# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cat',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='cat_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]