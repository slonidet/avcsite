# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-26 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_eventsdocuments'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='address',
            field=models.CharField(default='\u041c\u043e\u0441\u043a\u0432\u0430', max_length=300, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='events',
            name='link_event',
            field=models.CharField(default='#', max_length=300, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u043e\u0431\u044b\u0442\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='events',
            name='place',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f(\u0433\u043e\u0440\u043e\u0434/\u043f\u043e\u0441\u043e\u043b\u0451\u043a/\u0441\u0435\u043b\u043e/\u0442.\u043f)'),
        ),
    ]