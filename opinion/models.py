# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

class Opinion(models.Model):
	photo = models.ImageField(verbose_name='Фото')
	name = models.CharField(max_length=120, verbose_name=u'Имя Фамилия')
	desc = models.CharField(max_length=120, verbose_name=u'Вид деятельности', blank=True)
	text = RichTextField(verbose_name=u'Мнение')

	class Meta:
		verbose_name = u"Мнение"
		verbose_name_plural = u"Мнения"