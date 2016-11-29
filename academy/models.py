# -*- coding: utf-8 -*
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from imagekit.models import ProcessedImageField,ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from pilkit.processors.base import Anchor
# Create your models here.
class Experts(models.Model):
    name = models.CharField(max_length=350, verbose_name="Ф.И.О")
    photo = models.ImageField(upload_to='experts/',verbose_name=u'Фото')
    thumb =  ImageSpecField(source='photo',processors=[ResizeToFill(200, 200,anchor=Anchor.CENTER)],format='JPEG',options={'quality': 100})
    desc = models.CharField(max_length=300, verbose_name=u'Вид деятельности', blank=True)
    
    def __unicode__(self):
		return self.name

    class Meta:
		verbose_name = u"Эксперт"
		verbose_name_plural = u"Эксперты"

class AcademySlider(models.Model):
    title = models.CharField(max_length=350, verbose_name="Название")
    photo = models.ImageField(upload_to='academy_exprets/',verbose_name=u'Фото')
    thumb =  ImageSpecField(source='photo',processors=[ResizeToFill(500, 250,anchor=Anchor.CENTER)],format='JPEG',options={'quality': 100})
    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Фото(слайдер)"
		verbose_name_plural = u"Фото(слайдер)"

class Materials(models.Model):
    title = models.CharField(max_length=350, verbose_name="Название")
    video = models.CharField(max_length=600, verbose_name="Ссылка на видео-ресурс", blank=True)
    lecture = models.FileField(upload_to="documents/", verbose_name="Лекция", blank=True)
    presentation = models.FileField(upload_to="documents/", verbose_name="Презентация", blank=True)
    
    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Материал"
		verbose_name_plural = u"Материалы"

class Webinars(models.Model):
    title = models.CharField(max_length=350, verbose_name="Название")
    img = ProcessedImageField(upload_to='webinars',
                                           processors=[ResizeToFit(300, 200)],
                                           format='JPEG',
                                           options={'quality': 100}, blank=True, verbose_name="Изображение")
    teacher = models.CharField(max_length=350, verbose_name="Преподаватель")
    webinar = models.CharField(max_length=600, verbose_name="Ссылка на вебинар")
    date = models.DateTimeField(verbose_name='Дата проведения',auto_now_add=False, default=datetime.now)
    
    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Вебинар"
		verbose_name_plural = u"Вебинары"
