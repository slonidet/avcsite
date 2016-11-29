# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from .models import NewsLetter, NewsImages, PressReleases, PressImages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

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
            (DFO,u'Дальневосточный федеральный округ'))

def all_news(request):
    date_start = ""
    date_end = ""
    region_id = None
    news_list = NewsLetter.objects.all()
    if not(request.GET.get('date_start') or request.GET.get('date_end') or request.GET.get('region')):
        news_list = NewsLetter.objects.filter(published=True).order_by('-date_published')
    else:
        if request.GET.get('date_start'):
            try:
                date_start = request.GET.get('date_start')
                date_start_list = date_start.split(".")
                date_start = datetime(int(date_start_list[2]), int(date_start_list[1]), int(date_start_list[0]), 0, 0, 0)
            except:
                date_start = ""
        if request.GET.get('date_end'):
            try:
                date_end = request.GET.get('date_end')
                date_end_list = date_end.split(".")
                date_end = datetime(int(date_end_list[2]), int(date_end_list[1]), int(date_end_list[0]), 23, 59, 59)
            except:
                date_end = ""
        if request.GET.get('region'):
            region_id = request.GET.get('region')
            news_list = NewsLetter.objects.filter(okrug = region_id)
            
        if not date_start and date_end:
            date_start = datetime(int(date_end_list[2]), int(date_end_list[1]), int(date_end_list[0]), 0, 0, 0)
        if not date_end and date_start:
            date_end = datetime(int(date_start_list[2]), int(date_start_list[1]), int(date_start_list[0]), 23 , 59, 59)
            
        if date_start > date_end:
            date_start,date_end = date_end,date_start
        
        if date_start and date_start:
            news_list = news_list.filter(date_published__range=[date_start, date_end])
        
        
        news_list = news_list.filter(published=True).order_by('-date_published')
    
        
        
    paginator = Paginator(news_list,10)
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1
    
    
        
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    
    index = news.number
    last_index = paginator.num_pages 
    
    if index>4:
        min_index = index-4
    else:
        min_index = 0

    if  index<last_index:
        max_index = index+4
    else:
        max_index = last_index

    last_page = last_index-4

    return render(request, "allnews.html", {"news": news, "okruga":FED_OKR, "title":u"Новости Ассоциации","min_index":min_index,"max_index":max_index,"last_page":last_page})

def one_new(request, news_pk=1):

	news = NewsLetter.objects.get(id=news_pk)
	images = NewsImages.objects.filter(news_id=news_pk)
	other_news = NewsLetter.objects.exclude(id=news_pk).filter(published=True).order_by('-date_published')[:5]
	return render(request,"news.html", {"news": news, "images": images, "other": other_news,"title": news.title})

def okrug_news(request, okrug_name="CFO", page=1):
    news_list = NewsLetter.objects.filter(okrug=okrug_name,published=True,center_id=None).order_by('-date_published')
    paginator = Paginator(news_list,10)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    
    index = news.number
    last_index = paginator.num_pages 
    
    if index>4:
        min_index = index-4
    else:
        min_index = 0

    if  index<last_index:
        max_index = index+4
    else:
        max_index = last_index

    last_page = last_index-4 

    return render_to_response("okrug_news.html", {"news": news, "okruga":FED_OKR, "title":u"Новости Ассоциации", "okrug": okrug_name,"min_index":min_index,"max_index":max_index,"last_page":last_page})



def center_news(request,center_pk=1, page=1):

    news_list = NewsLetter.objects.filter(center_id=center_pk,published=True).order_by('-date_published')
    paginator = Paginator(news_list,10)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    
    index = news.number
    last_index = paginator.num_pages 
    
    if index>4:
        min_index = index-4
    else:
        min_index = 0

    if  index<last_index:
        max_index = index+4
    else:
        max_index = last_index
    
    last_page = last_index-4 

    return render_to_response("center_news.html", {"news":news,"okruga":FED_OKR, "title":u"Новости центра","center":center_pk,"min_index":min_index,"max_index":max_index,"last_page":last_page})

def all_releases(request, page=1):
    releases_list = PressReleases.objects.all().order_by('-press_date')
    paginator = Paginator(releases_list,10)

    try:
        releases = paginator.page(page)
    except PageNotAnInteger:
        releases = paginator.page(1)
    except EmptyPage:
        releases = paginator.page(paginator.num_pages)
    
    index = releases.number
    last_index = paginator.num_pages 
    
    if index>4:
        min_index = index-4
    else:
        min_index = 0

    if  index<last_index:
        max_index = index+4
    else:
        max_index = last_index
    
    last_page = last_index-4 

    return render_to_response("press_releases.html", {"releases": releases,"title":u"Пресс-релизы Ассоциации","min_index":min_index,"max_index":max_index,"last_page":last_page})

def one_release(request, release_pk=1):

	release = PressReleases.objects.get(id=release_pk)
	images = PressImages.objects.filter(releases_id=release_pk)
	other_releases = PressReleases.objects.exclude(id=release_pk).order_by('-press_date')[:5]
	return render_to_response("press_release.html", {"release": release, "images": images, "other": other_releases,"title":release.title})

