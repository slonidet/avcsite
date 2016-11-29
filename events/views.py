# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Events, EventsImages, EventsDocuments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

# Create your views here.
def all_events(request, page=1):
    events_list = Events.objects.order_by('-date_event').filter(published=True)
    paginator = Paginator(events_list,12)

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    index = events.number
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

    return render(request,'all_events.html',{'events':events, "okruga":FED_OKR, "title":u"События","min_index":min_index,"max_index":max_index,"last_page":last_page})

def one_event(request, event_pk):
    event = Events.objects.get(id=event_pk)
    images = EventsImages.objects.filter(news_id=event.pk)
    documents = EventsDocuments.objects.filter(events_id=event.pk)
    other_event = Events.objects.exclude(id=event_pk).filter(published=True).order_by('-date_event')[:5]
    return render(request,'event.html',{'event':event, 'images':images,'documents':documents, 'other':other_event, 'title':event.title})

def okrug_events(request, okrug_name="CFO",page=1):
    events_list = Events.objects.filter(okrug=okrug_name,center_id=None,published=True).order_by('-date_event')
    paginator = Paginator(events_list,10)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    index = events.number
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

    return render(request,'okrug_events.html',{'events':events, "okruga":FED_OKR, "title":u"События","okrug":okrug_name,"min_index":min_index,"max_index":max_index,"last_page":last_page})

def center_events(request, center_pk=1, page=1):
    events_list= Events.objects.filter(center_id=center_pk,published=True).order_by('-date_event')

    paginator = Paginator(events_list,10)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    index = events.number
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

    return render(request,'center_events.html',{'events':events, "okruga":FED_OKR, "title":u"События","center":center_pk,"min_index":min_index,"max_index":max_index,"last_page":last_page})

def test_events(request, page=1):
    events_list = Events.objects.order_by('-date_event').filter(center_id=None, published=True)
    paginator = Paginator(events_list,10)

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    index = events.number
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

    return render(request,'test_events.html',{'events':events, "okruga":FED_OKR, "title":u"События","min_index":min_index,"max_index":max_index,"last_page":last_page})