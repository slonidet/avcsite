# -*- coding: utf-8 -*-
from django import template

register = template.Library()

#Фильтр получает значение из словаря по ключу
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)