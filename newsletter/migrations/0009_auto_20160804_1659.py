# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-04 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_auto_20160804_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', '\u0427\u0435\u0440\u043d\u043e\u0432\u0438\u043a'), ('sent', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u043d\u0430 \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u044e'), ('agreed', '\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u0430'), ('ready', '\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0430 \u043a \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')], max_length=20, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441'),
        ),
    ]
