# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-17 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='lecture',
            field=models.FileField(blank=True, upload_to='documents/', verbose_name='\u041b\u0435\u043a\u0446\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='presentation',
            field=models.FileField(blank=True, upload_to='documents/', verbose_name='\u041f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='video',
            field=models.CharField(blank=True, max_length=600, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e-\u0440\u0435\u0441\u0443\u0440\u0441'),
        ),
    ]
