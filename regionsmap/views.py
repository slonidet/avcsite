# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Centers, Regions
from newsletter.models import NewsLetter
from content.models import Projects
from events.models import Events
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def centers(request):
    regions = Regions.objects.all()
    centers= Centers.objects.all()

    return render(request, "centers.html", {"centers":centers,"regions":regions})
    
    

def center(request, center_pk=1):
    center = Centers.objects.get(id=center_pk)
    news = NewsLetter.objects.filter(published=True,center_id=center_pk).order_by('-date_published')[:3]
    projects = Projects.objects.filter(published=True,center_id=center_pk).order_by('title')[:3]
    events = Events.objects.filter(published=True,center_id=center_pk).order_by('-date_event')[:6]
    return render(request, "center.html", {"center": center, "news":news, "projects":projects, "events": events})