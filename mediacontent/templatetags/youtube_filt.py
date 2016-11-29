# -*- coding: utf-8 -*-
from django import template
register = template.Library()

#превью для видео с ютуба
@register.filter
def youtube_filt(text):
    text = text.replace("https://","")
    text = text.split("/")
    source = text[1].replace("watch?v=","")
    return "//img.youtube.com/vi/"+ source + "/mqdefault.jpg"

@register.filter
def embed_filt(text):
    text = text.replace("https://","")
    text = text.split("/")
    text[0] = text[0]+ "/embed/"
    text[0] = text[0].replace("youtu.be","www.youtube.com")
    text[1] = text[1].replace("watch?v=","")
    return "https://"+ text[0] + text[1]