#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

class Album(models.Model):
    thumb = ProcessedImageField(upload_to='thumb',
								processors=[ResizeToFill(320, 180)],
								format='JPEG',
								options={'quality': 80}, verbose_name=u'Превью')

    title = models.CharField(verbose_name='Название альбома', max_length=255)
    date_album = models.DateTimeField(verbose_name='Дата',auto_now_add=False, default=datetime.now)
    desc = RichTextField(verbose_name='Описание альбома', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

class AlbumPhoto(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField("Название", max_length=250)
    img = models.ImageField("Фото", upload_to='mediacontent/')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

class Video(models.Model):
    title = models.CharField("Название", max_length=250)
    source = models.CharField("Ссылка", max_length=250)
    date = models.DateTimeField(verbose_name='Дата',auto_now_add=False, default=datetime.now)
    desc = models.TextField(verbose_name='Описание видео',blank=True)
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"