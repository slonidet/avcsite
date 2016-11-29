# -*- coding: utf-8 -*
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ProcessedImageField,ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from pilkit.processors.base import Anchor

class Experts(models.Model):
    name = models.CharField(max_length=350, verbose_name="Ф.И.О")
    photo = models.ImageField(upload_to='experts/',verbose_name=u'Фото')
    thumb =  ImageSpecField(source='photo',processors=[ResizeToFill(200, 200,anchor=Anchor.CENTER)],format='JPEG',options={'quality': 100})
    position = models.CharField(max_length=10,verbose_name=u'Порядковый номер', default=99)
    desc = models.CharField(max_length=300, verbose_name=u'Вид деятельности', blank=True)
    
    
    def __unicode__(self):
		return self.name

    class Meta:
		verbose_name = u"Эксперт"
		verbose_name_plural = u"Эксперты"
    
class Materials(models.Model):
    title = models.CharField(max_length=350, verbose_name="Название")
    material = models.FileField(upload_to="documents/", verbose_name="Материал")

    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Материал"
		verbose_name_plural = u"Материалы"