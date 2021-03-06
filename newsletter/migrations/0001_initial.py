# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 10:19
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regionsmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('img', models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='thumb', verbose_name='\u041f\u0440\u0435\u0432\u044c\u044e')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('okrug', models.CharField(choices=[('CFO', '\u0426\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('NWFO', '\u0421\u0435\u0432\u0435\u0440\u043e-\u0417\u0430\u043f\u0430\u0434\u043d\u044b\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('YFO', '\u042e\u0436\u043d\u044b\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('CSFO', '\u0421\u0435\u0432\u0435\u0440\u043e-\u041a\u0430\u0432\u043a\u0430\u0437\u0441\u043a\u0438\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('PFO', '\u041f\u0440\u0438\u0432\u043e\u043b\u0436\u0441\u043a\u0438\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('UFO', '\u0423\u0440\u0430\u043b\u044c\u0441\u043a\u0438\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('SFO', '\u0421\u0438\u0431\u0438\u0440\u0441\u043a\u0438\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('DFO', '\u0414\u0430\u043b\u044c\u043d\u0435\u0432\u043e\u0441\u0442\u043e\u0447\u043d\u044b\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('KFO', '\u041a\u0440\u044b\u043c\u0441\u043a\u0438\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433')], default='CFO', max_length=4, verbose_name='\u041e\u043a\u0440\u0443\u0433')),
                ('published', models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e?')),
                ('center_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='regionsmap.Centers', verbose_name='\u0426\u0435\u043d\u0442\u0440')),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='PressImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('img', models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='PressReleases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='thumb', verbose_name='\u041f\u0440\u0435\u0432\u044c\u044e')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('press_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u0435\u0441\u0441-\u0440\u0435\u043b\u0438\u0437\u0430')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u0441\u0441 \u0440\u0435\u043b\u0438\u0437',
                'verbose_name_plural': '\u041f\u0440\u0435\u0441\u0441 \u0440\u0435\u043b\u0438\u0437\u044b',
            },
        ),
        migrations.AddField(
            model_name='pressimages',
            name='releases',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.PressReleases'),
        ),
        migrations.AddField(
            model_name='newsimages',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.NewsLetter'),
        ),
    ]
