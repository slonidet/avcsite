# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20160704_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='label',
            field=models.CharField(default='-', max_length=50, verbose_name='\u041f\u043e\u043c\u0435\u0442\u043a\u0430'),
        ),
    ]
