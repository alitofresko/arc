# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_auto_20171025_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='members/'),
        ),
    ]