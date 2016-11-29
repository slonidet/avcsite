# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-25 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_remove_projects_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='direction',
            field=models.CharField(choices=[('SOC', '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435'), ('SOB', '\u0421\u043e\u0431\u044b\u0442\u0438\u0439\u043d\u043e\u0435'), ('MED', '\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0435'), ('KUL', '\u041a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e-\u043f\u0440\u043e\u0441\u0432\u0435\u0442\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0435'), ('KOR', '\u041a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u043e\u0435'), ('SER', '\u0421\u0435\u0440\u0435\u0431\u0440\u044f\u043d\u043e\u0435'), ('OBR', '\u0412 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0438'), ('OTH', '\u0414\u0440\u0443\u0433\u043e\u0435')], default='OTH', max_length=5, verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
        ),
    ]
