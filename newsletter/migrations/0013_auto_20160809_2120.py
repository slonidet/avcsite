# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-09 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0012_auto_20160804_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='status',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='status_admin',
            field=models.BooleanField(default=False, verbose_name='\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u043e'),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='status_chempionat',
            field=models.BooleanField(default=False, verbose_name='\u0420\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u043a \u043f\u0443\u0431\u043b\u0438\u043a\u0446\u0438\u0438'),
        ),
    ]
