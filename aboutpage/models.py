# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit,ResizeToFill
# Create your models here.
class Structure(models.Model):
    struc_arr = (('sov',u"Совет"), ('dir',u'Дирекция'))
    struc_soviet = models.CharField(verbose_name=u'Относится к', max_length=4,
                                      choices=struc_arr, default='sov')
    img = ProcessedImageField(verbose_name=u"Изображание", processors=[ResizeToFill(300,300, anchor='t')],
                                           format='JPEG',
                                           options={'quality': 100})


    full_name = models.CharField(verbose_name="Ф.И.О.", max_length=200)
    is_major = models.BooleanField(verbose_name=u"Директор/глава совета", default=False)
    position = models.IntegerField(blank=True, null=True, verbose_name="Позиция", )
    desc = models.CharField(verbose_name=u"Должность", max_length=300)
    about = models.TextField(verbose_name="Информация")

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = "Член структуры"
        verbose_name_plural = "Члены структуры"

class Contacts(models.Model):
    city = models.CharField(verbose_name="Город", default="Москва", max_length=100)
    address = models.CharField("Адрес", max_length=250)
    metro = models.CharField("Станция метро", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email", max_length=100)
    zip_code = models.CharField("Индекс", max_length=20, blank=True)
    map_con = models.TextField("Карта", blank=True)

    def __unicode__(self):
        return "Контакты"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"