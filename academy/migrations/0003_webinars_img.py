# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-17 09:24
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_auto_20161017_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinars',
            name='img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='webinars'),
        ),
    ]