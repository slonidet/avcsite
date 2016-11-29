# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField,ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from regionsmap.models import Centers
import datetime
from pilkit.processors.base import Anchor


class Opinion(models.Model):
    photo = ProcessedImageField(upload_to='opinion/',
        	processors=[ResizeToFit(600, 400,anchor=Anchor.CENTER,mat_color="white")],
        	format='JPEG',
        	options={'quality': 100}, verbose_name=u'Фото')
    thumb =  ImageSpecField(source='photo',processors=[ResizeToFit(300, 300,anchor=Anchor.CENTER)],format='JPEG',options={'quality': 90})
    home_thumb =  ImageSpecField(source='photo',processors=[ResizeToFit(200, 150,anchor=Anchor.CENTER)],format='JPEG',options={'quality': 90})
    name = models.CharField(max_length=90, verbose_name=u'Имя')
    fam = models.CharField(max_length=100, verbose_name=u'Фамилия', blank=True)
    desc = models.CharField(max_length=300, verbose_name=u'Вид деятельности', blank=True)
    date = models.DateField(verbose_name="Дата", default=datetime.date.today)
    quote = models.TextField(verbose_name="Цитата", blank=True)
    text = RichTextField(verbose_name=u'Мнение', blank=True)

    def __unicode__(self):
	    return self.name + " " +self.fam

    class Meta:
		verbose_name = u"Мнение"
		verbose_name_plural = u"Мнения"

class Partners(models.Model):
    banner = models.ImageField(verbose_name='Баннер',upload_to='logo/')
    thumb =  ImageSpecField(source='banner',processors=[ResizeToFit(300, 300, anchor=Anchor.CENTER,mat_color=True,upscale=False)],format='JPEG',options={'quality': 100})
    name = models.CharField(max_length=250, verbose_name=u'Название', default="Без названия")
    
    description = RichTextField("Описание", default="Описание отсутствует")
    source = models.CharField(max_length=120, verbose_name='Ссылка')
    position = models.IntegerField(verbose_name="Позиция", default=1)
    
    def __unicode__(self):
	    return self.name

    class Meta:
		verbose_name = u"Партнёр"
		verbose_name_plural = u"Партнёры"

class History(models.Model):
    photo = ProcessedImageField(upload_to='history/',
            processors=[ResizeToFit(600, 400,anchor=Anchor.CENTER)],format='JPEG',
            options={'quality': 100}, verbose_name=u'Фото')
    thumb =  ImageSpecField(source='photo',processors=[ResizeToFill(300, 200, anchor=Anchor.CENTER)],format='JPEG',options={'quality': 90})
    home_thumb =  ImageSpecField(source='photo',processors=[ResizeToFit(200, 150,anchor=Anchor.CENTER)],format='JPEG',options={'quality': 90})
    name = models.CharField(max_length=90, verbose_name=u'Имя')
    fam = models.CharField(max_length=100, verbose_name=u'Фамилия', blank=True)
    desc = models.CharField(max_length=300, verbose_name=u'Вид деятельности', blank=True)
    date = models.DateField(verbose_name="Дата", default=datetime.date.today)
    quote = models.TextField(verbose_name="Цитата", blank=True)
    text = RichTextField(verbose_name=u'История',blank=True)

    def __unicode__(self):
	    return self.name + " " +self.fam

    class Meta:
		verbose_name = u"История успеха"
		verbose_name_plural = u"Истории успеха"

class Slider(models.Model):
    source = models.CharField(max_length=250, verbose_name='Ссылка', default="#")
    image = models.ImageField(verbose_name='Фото', upload_to='slider/')
    name = models.CharField(max_length=50, verbose_name=u'Название',default="Без названия")
    def __unicode__(self):
	    return self.name

    class Meta:
		verbose_name = u"Изображение(слайдер)"
		verbose_name_plural = u"Изображения(слайдер)"

class Projects(models.Model):
    
    SOC = 'SOC'
    SOB = 'SOB'
    MED = 'MED'
    KUL = 'KUL'
    KOR = 'KOR'
    SER = 'SER'
    OBR = 'OBR'
    OTH = 'OTH'

    DIRECTIONS = ((SOC,u'Социальное'),(SOB,u'Событийное'),(MED,u'Медицинское'), (KUL,u'Культурно-просветительское'), 
                (KOR,u'Корпоративное'),(SER,u'Серебряное'),(OBR,u'В образовании'), (OTH,u'Другое'))

    img =  ProcessedImageField(upload_to='thumb',
								processors=[ResizeToFit(300, 200)],
								format='JPEG',
								options={'quality': 90}, verbose_name=u'Превью')
    title = models.CharField(max_length=350, verbose_name='Название')
    description = RichTextField(verbose_name="Описание")
    direction = models.CharField(max_length=5, verbose_name='Направление проекта', default=OTH, choices=DIRECTIONS)
    center_id = models.ForeignKey(Centers, blank=True, null=True, verbose_name="Центр")
    published = models.BooleanField(default=False, verbose_name='Опубликовано?')
    label = models.CharField(verbose_name="Пометка",max_length=50, default="-")
    

    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Проект"
		verbose_name_plural = u"Проекты"

class ProjectsImages(models.Model):

	project = models.ForeignKey(Projects)
	title = models.CharField(max_length=255, verbose_name=u'Название')
	img = models.ImageField(verbose_name=u"Изображание", upload_to='projects/')

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u"Изображение"
		verbose_name_plural = u"Изображения"

class Documents(models.Model):
    title = models.CharField(max_length=350, verbose_name="Название")
    document = models.FileField(upload_to="documents/", verbose_name="Документ")

    def __unicode__(self):
		return self.title

    class Meta:
		verbose_name = u"Документ"
		verbose_name_plural = u"Документы"

class VideoHomePage(models.Model):
    title = models.CharField("Название", max_length=250)
    source = models.CharField("Ссылка", max_length=250)
    date_add = models.DateTimeField(verbose_name='Дата',auto_now_add=True)
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Видео(Для главной страницы)"
        verbose_name_plural =  "Видео(Для главной страницы)"
