# -*- coding: utf-8 -*-
from django import template
import os

register = template.Library()

#Фильтр получает значение из словаря по ключу
@register.filter
def ext_filt(file):
    filename, file_extension = os.path.splitext(file)
    return file_extension[1:]