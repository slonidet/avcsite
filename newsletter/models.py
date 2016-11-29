# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from datetime import datetime
from regionsmap.models import Centers
from content.models import Documents


class Rubrics(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Название рубрики')
    
    def __unicode__(self):
		return self.title

    class Meta:
        verbose_name = u"Рубрика"
        verbose_name_plural = u"Рубрики"


class NewsLetter(models.Model):
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
    
    #news_status = [("draft","Черновик"),("sent","Отправлена на модерацию"),("agreed","Согласована"),("ready","Разрешена к публикации")]
    

    thumb = ProcessedImageField(upload_to='thumb',
								processors=[ResizeToFill(300, 200)],
								format='JPEG',
								options={'quality': 80}, verbose_name=u'Превью')
    title = models.CharField(max_length=350, verbose_name='Заголовок')
    text = RichTextField(verbose_name='Текст')
    news_docments = models.ForeignKey(Documents, verbose_name="Прикрепить документ", blank=True, null=True)
    date_published = models.DateTimeField(verbose_name='Дата публикации',auto_now_add=False, default=datetime.now)
    okrug = models.CharField(verbose_name='Округ', max_length=4,
                                      choices=FED_OKR,
                                      default=CFO)
    center_id = models.ForeignKey(Centers, blank=True, null=True, verbose_name="Центр")
    
    fes_news = models.BooleanField(default=False, verbose_name='Новость Федерального экспертного совета')
    published = models.BooleanField(default=False, verbose_name='Опубликовано?')
    label = models.CharField(verbose_name="Пометка",max_length=50, default="-")
    rubric = models.ForeignKey(Rubrics, verbose_name="Рубрика", blank=True, null=True)
    #status = models.CharField(verbose_name="Статус", max_length = 20, choices=news_status, blank=True, null=True)
    status_admin = models.BooleanField(default=False, verbose_name='Согласовано')
    status_chempionat = models.BooleanField(default=False, verbose_name='Разрешить к публикции')
    
    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Новость"
		verbose_name_plural = u"Новости"


class NewsImages(models.Model):

	news = models.ForeignKey(NewsLetter)
	title = models.CharField(max_length=255, verbose_name=u'Название')
	img = models.ImageField(verbose_name=u"Изображание")

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u"Изображение"
		verbose_name_plural = u"Изображения"

class PressReleases(models.Model):
    thumb = ProcessedImageField(upload_to='thumb',
								processors=[ResizeToFill(159, 100)],
								format='JPEG',
								options={'quality': 80}, verbose_name=u'Превью')
    title = models.CharField(max_length=350, verbose_name=u'Заголовок')
    text = RichTextField(verbose_name='Текст')
    press_date = models.DateTimeField(verbose_name='Дата пресс-релиза',auto_now_add=False, default=datetime.now)

    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Пресс релиз"
		verbose_name_plural = u"Пресс релизы"

class PressImages(models.Model):

	releases = models.ForeignKey(PressReleases)
	title = models.CharField(max_length=255, verbose_name=u'Название')
	img = models.ImageField(verbose_name=u"Изображание")

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u"Изображение"
		verbose_name_plural = u"Изображения"
		

    