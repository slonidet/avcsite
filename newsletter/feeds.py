# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.syndication.views import Feed
from .models import NewsLetter

class NewsRSS(Feed):
    title = "Новости АВЦ"
    description = "Новостная лента сайта Ассоциации волонтёрских центров"
    link = "/news/"
    
    def items(self):
        return NewsLetter.objects.filter(published=True).order_by('-date_published')[:25]
    
    def item_link(self, item):
        return "/news/view/"+str(item.id)
    
    def item_title(self,item):
        return item.title
    
    def item_description(self,item):
        return item.text