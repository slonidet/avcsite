# -*- coding: utf-8 -*-
from django import template
import re
register = template.Library()

#фильтр убирает лишние пробелы для вывода короткого текста
@register.filter
def text_filt(text):
    newtext = text.replace("&nbsp;", " ")
    newtext = newtext.lstrip()
    return re.sub(r'\s+', ' ',newtext)