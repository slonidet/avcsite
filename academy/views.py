# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import AcademyForm
from django.core.mail import send_mail
from django.conf import settings
from regionsmap.models import Regions
import json
from django.http import HttpResponse
from .models import *
# Create your views here.


def academy(request):
    
    webinars = Webinars.objects.order_by('-date')[:3]
    experts = Experts.objects.all()
    materials = Materials.objects.all()
    images = AcademySlider.objects.all()
    
    if request.POST:
        form = AcademyForm(request.POST)
        
        if form.is_valid():
            message = u"Успех!"
    
    else:
        form = AcademyForm()
        
    return render(request, "academy.html", {"form":form, "webinars":webinars, "experts":experts, "materials":materials, "images":images, "title":"Академия волонтёрских центров"})
    
def write(request):
    if request.POST:
        form = AcademyForm(request.POST)
        if request.is_ajax():
            data = ""
            if form.is_valid():
                
                regions = [(region.key, region.title) for region in Regions.objects.all()]

                for obj in regions:
                    if obj[0] == request.POST['region']:
                        region = obj[1]
                        break
                
                name = request.POST['name']
                webinar = request.POST['webinar']
                idea = request.POST['idea']
                
                message = "Регион: {} \n" \
                        "Ф.И.О: {} \n" \
                        "Является участником вебинара: {} \n" \
                        "Сообщение: {} \n".format(region, name, webinar, idea)
                
                try:
                    send_mail("Идеи и предложения",message,settings.EMAIL_HOST_USER,["info@avcrf.ru"])
                    data = {"message":"Сообщение успешно отправлено!", "errors":"False" }
                except:
                    data = {"message":"Произошла ошибка при отправке,пожалуйста,попробуйте позже.", "errors":"True"}
            else:
                data = {"message":"Убедитесь,что вы заполнили все обязательные поля!", "errors":"True" }
        return HttpResponse(json.dumps(data, ensure_ascii=False,encoding='utf8'), content_type='application/json')