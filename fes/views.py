# -*- coding: utf-8 -*-

from django.shortcuts import render
from content.models import Documents
from newsletter.models import NewsLetter
from .models import Experts, Materials
# Create your views here.

def fes_view(request):
    experts = Experts.objects.all().order_by('position')
    materials = Materials.objects.all()
    news = NewsLetter.objects.filter(fes_news=True).order_by('-date_published')[:5]
    
    return render(request,"fes.html", {"materials": materials,"activity":news, "experts":experts, "title":"Экспертный совет"})
