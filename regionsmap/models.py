# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit,ResizeToCover

class Regions(models.Model):
    key = models.CharField(max_length = 5, verbose_name=u"Код",primary_key=True)
    title = models.CharField(max_length=50, verbose_name=u"Название")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Регион"
        verbose_name_plural = u"Регионы"
        ordering = ['title']

class Centers(models.Model):
    source = models.CharField(max_length=250,verbose_name=u"Ссылка", default="#")
    account = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Аккаунт центра")
    dobro_link = models.CharField(max_length=350,verbose_name=u"Ссылка на страницу добровольцы.рф", default="#")
    region = models.ForeignKey(Regions, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.CharField(verbose_name="Город/село/т.п.", max_length=30, blank=True)
    title = models.CharField(max_length=400, verbose_name=u"Название центра")
    image = models.ImageField("Изображение", blank=True)
    thumb = ImageSpecField(source='image',
                                      processors=[ResizeToFit(200, 200,mat_color="white",anchor='c')],
                                      format='JPEG',
                                      options={'quality': 80})
    desc = models.TextField("Описание", blank=True)
    director = models.CharField(max_length=250, verbose_name=u"Руководитель",blank=True)
    sub_director = models.CharField(max_length=250, verbose_name=u"Заместитель", blank=True)
    phone_number = models.CharField(max_length=20, verbose_name=u"Телефон", blank=True)
    email = models.CharField(max_length=100, verbose_name=u"Email", blank=True)
    address = models.CharField(max_length=250, verbose_name=u"Адрес", blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Центр"
        verbose_name_plural = u"Центры"
        ordering = ['title']
