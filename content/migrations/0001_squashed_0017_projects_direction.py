# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-25 11:05
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    replaces = [(b'content', '0001_initial'), (b'content', '0002_auto_20160627_1004'), (b'content', '0003_auto_20160627_1008'), (b'content', '0004_history_desc'), (b'content', '0005_auto_20160628_2155'), (b'content', '0006_history_quote'), (b'content', '0007_opinion_quote'), (b'content', '0008_auto_20160628_2223'), (b'content', '0009_partners_position'), (b'content', '0010_auto_20160704_1822'), (b'content', '0011_auto_20160704_1850'), (b'content', '0012_auto_20160704_1852'), (b'content', '0013_auto_20160707_1415'), (b'content', '0014_videohomepage'), (b'content', '0015_partners_teamwork'), (b'content', '0016_remove_partners_teamwork'), (b'content', '0017_projects_direction')]

    initial = True

    dependencies = [
        ('regionsmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('document', models.FileField(upload_to='documents/', verbose_name='\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to='history/', verbose_name='\u0424\u043e\u0442\u043e')),
                ('name', models.CharField(max_length=90, verbose_name='\u0418\u043c\u044f')),
                ('fam', models.CharField(blank=True, max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='\u0418\u0441\u0442\u043e\u0440\u0438\u044f')),
                ('desc', models.CharField(blank=True, max_length=300, verbose_name='\u0412\u0438\u0434 \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='\u0414\u0430\u0442\u0430')),
                ('quote', models.TextField(blank=True, verbose_name='\u0426\u0438\u0442\u0430\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0443\u0441\u043f\u0435\u0445\u0430',
                'verbose_name_plural': '\u0418\u0441\u0442\u043e\u0440\u0438\u0438 \u0443\u0441\u043f\u0435\u0445\u0430',
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to='opinion/', verbose_name='\u0424\u043e\u0442\u043e')),
                ('name', models.CharField(max_length=90, verbose_name='\u0418\u043c\u044f')),
                ('fam', models.CharField(blank=True, max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('desc', models.CharField(blank=True, max_length=300, verbose_name='\u0412\u0438\u0434 \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='\u041c\u043d\u0435\u043d\u0438\u0435')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='\u0414\u0430\u0442\u0430')),
                ('quote', models.TextField(blank=True, verbose_name='\u0426\u0438\u0442\u0430\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u043d\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041c\u043d\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='logo/', verbose_name='\u0411\u0430\u043d\u043d\u0435\u0440')),
                ('name', models.CharField(default='\u0411\u0435\u0437 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f', max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(default='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('source', models.CharField(max_length=120, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('position', models.IntegerField(default=1, verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041f\u0430\u0440\u0442\u043d\u0451\u0440',
                'verbose_name_plural': '\u041f\u0430\u0440\u0442\u043d\u0451\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', imagekit.models.fields.ProcessedImageField(upload_to='thumb', verbose_name='\u041f\u0440\u0435\u0432\u044c\u044e')),
                ('title', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('center_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='regionsmap.Centers', verbose_name='\u0426\u0435\u043d\u0442\u0440')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0435\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ProjectsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('img', models.ImageField(upload_to='projects/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0430\u043d\u0438\u0435')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Projects')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(default='#', max_length=250, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('image', models.ImageField(upload_to='slider/', verbose_name='\u0424\u043e\u0442\u043e')),
                ('name', models.CharField(default='\u0411\u0435\u0437 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f', max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435(\u0441\u043b\u0430\u0439\u0434\u0435\u0440)',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f(\u0441\u043b\u0430\u0439\u0434\u0435\u0440)',
            },
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=350, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='projects',
            name='label',
            field=models.CharField(default='-', max_length=50, verbose_name='\u041f\u043e\u043c\u0435\u0442\u043a\u0430'),
        ),
        migrations.AddField(
            model_name='projects',
            name='published',
            field=models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e?'),
        ),
        migrations.CreateModel(
            name='VideoHomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('source', models.CharField(max_length=250, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u0412\u0438\u0434\u0435\u043e(\u0414\u043b\u044f \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b)',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e(\u0414\u043b\u044f \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b)',
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='direction',
            field=models.CharField(choices=[('soc', '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435'), ('sob', '\u0421\u043e\u0431\u044b\u0442\u0438\u0439\u043d\u043e\u0435'), ('med', '\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0435'), ('kul', '\u041a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e-\u043f\u0440\u043e\u0441\u0432\u0435\u0442\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0435'), ('kor', '\u041a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u043e\u0435'), ('ser', '\u0421\u0435\u0440\u0435\u0431\u0440\u044f\u043d\u043e\u0435'), ('obr', '\u0412 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0438'), ('other', '\u0414\u0440\u0443\u0433\u043e\u0435')], default='other', max_length=4, verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
        ),
    ]