# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-26 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20161126_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='place',
            field=models.CharField(default='\u041c\u043e\u0441\u043a\u0432\u0430', max_length=100, verbose_name='\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f(\u0433\u043e\u0440\u043e\u0434/\u043f\u043e\u0441\u0451\u043b\u043e\u043a/\u0441\u0435\u043b\u043e/\u0442.\u043f)'),
        ),
    ]
