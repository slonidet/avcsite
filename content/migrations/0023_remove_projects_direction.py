# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-25 10:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_projects_direction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='direction',
        ),
    ]
