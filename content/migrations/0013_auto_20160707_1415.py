# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-07 11:15
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20160704_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(upload_to='history/', verbose_name='\u0424\u043e\u0442\u043e'),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(upload_to='opinion/', verbose_name='\u0424\u043e\u0442\u043e'),
        ),
    ]