# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-07 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regionsmap', '0007_auto_20160804_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='centers',
            name='city',
            field=models.CharField(blank=True, max_length=30, verbose_name='\u0413\u043e\u0440\u043e\u0434/\u0441\u0435\u043b\u043e/\u0442.\u043f.'),
        ),
    ]