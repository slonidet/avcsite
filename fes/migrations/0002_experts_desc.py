# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-12 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experts',
            name='desc',
            field=models.CharField(blank=True, max_length=300, verbose_name='\u0412\u0438\u0434 \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438'),
        ),
    ]
