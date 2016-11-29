# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from datetime import datetime
from regionsmap.models import Centers

class Events(models.Model):
    CFO = 'CFO'
    NWFO = 'NWFO'
    YFO = 'YFO'
    SCFO = 'CSFO'
    PFO = 'PFO'
    UFO = 'UFO'
    SFO = 'SFO'
    DFO = 'DFO'
    KFO = 'KFO'
    FED_OKR = ((CFO,u'Центральный федеральный округ'),
                (NWFO,u'Северо-Западный федеральный округ'),
                (YFO,u'Южный федеральный округ'),
                (SCFO,u'Северо-Кавказский федеральный округ'),
                (PFO,u'Приволжский федеральный округ'),
                (UFO,u'Уральский федеральный округ'),
                (SFO,u'Сибирский федеральный округ'),
                (DFO,u'Дальневосточный федеральный округ'),
                (KFO,u'Крымский федеральный округ'))


    img =  ProcessedImageField(upload_to='thumb',
								processors=[ResizeToFill(300, 200)],
								format='JPEG',
								options={'quality': 90}, verbose_name=u'Превью')
    title = models.CharField(verbose_name="Заголовок", max_length = 350)
    place = models.CharField(verbose_name="Место проведения(город/посёлок/село/т.п)", max_length=100, default="Москва" )
    address = models.CharField(verbose_name="Адрес проведения", max_length=300, blank=True )
    link_event = models.CharField(verbose_name="Ссылка на событие", max_length=300, default="#")
    okrug = models.CharField(verbose_name='Округ', max_length=4,
                                      choices=FED_OKR,
                                      default=CFO)
    center_id = models.ForeignKey(Centers, blank=True, null=True, verbose_name="Центр")
    text = RichTextField(verbose_name='Текст')
    date_event = models.DateTimeField(verbose_name='Дата события',auto_now_add=False, default=datetime.now)
    published = models.BooleanField(default=False, verbose_name='Опубликовано?')
    label = models.CharField(verbose_name="Пометка",max_length=50, default="-")
    
    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Событие"
		verbose_name_plural = u"События"

class EventsImages(models.Model):

	news = models.ForeignKey(Events)
	title = models.CharField(max_length=255, verbose_name=u'Название')
	img = models.ImageField(verbose_name=u"Изображание", upload_to='events/')

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u"Изображение"
		verbose_name_plural = u"Изображения"
		
class EventsDocuments(models.Model):

	events = models.ForeignKey(Events)
	title = models.CharField(max_length=255, verbose_name=u'Название')
	document = models.ImageField(verbose_name=u"Документ", upload_to='events_documents/')

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u"Документ(События)"
		verbose_name_plural = u"Документы(События)"
