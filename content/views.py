# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Projects, Documents, ProjectsImages, History, Opinion
from django.core.mail import EmailMessage
from django.conf import settings
from regionsmap.models import Regions
from .forms import FormCaptcha
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from events.models import Events

# Create your views here.
def develop(request):
    return render(request,"develop.html")

def write(request):

    if request.POST:
        form = FormCaptcha(request.POST)

        if form.is_valid():
            name = request.POST['name']
            fam= request.POST['2ndname']
            otch= request.POST['3rdname']
            phone = request.POST['phone']
            mail = request.POST['mail']
            text = request.POST['description']

            body = "Имя: {} \n" \
                "Фамилия: {} \n" \
                "Отчество: {} \n" \
                "Телефон: {} \n" \
                "Email: {} \n" \
                "Сообщение: {} \n".format(name, fam, otch, phone, mail, text)
            from_email = settings.EMAIL_HOST_USER
            to_email = ['info@avcrf.ru']
            email = EmailMessage(u'Обращение', body , from_email,to_email)

            if request.FILES:
                for file in request.FILES.getlist('files'):
                    email.attach(file.name, file.read())

            if email.send():
                return render(request,"write.html", {"success": "good","form":form})
            else:
                return render(request,"write.html", {"success": "errors","form":form})
        else:
            return render(request,"write.html", {"success": "errors","form":form})
    else:
        form = FormCaptcha()

    return render(request, "write.html", {"form":form})


def all_projects(request, page=1):
    SOC = 'SOC'
    SOB = 'SOB'
    MED = 'MED'
    KUL = 'KUL'
    KOR = 'KOR'
    SER = 'SER'
    OBR = 'OBR'
    OTH = 'OTH'

    DIRECTIONS = ((SOC,u'Социальное'),(SOB,u'Событийное'),(MED,u'Медицинское'), (KUL,u'Культурно-просветительское'), 
                (KOR,u'Корпоративное'),(SER,u'Серебряное'),(OBR,u'В образовании'), (OTH,u'Другое'))
                
    
    
    if request.GET.get("directions"):
        projects_list = Projects.objects.all().filter(published=True,direction=request.GET.get('directions'))
    else:
        projects_list = Projects.objects.all().filter(published=True)
    
    
    paginator = Paginator(projects_list,12)
    
    
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1
    

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    
    index = projects.number
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

    return render(request,"projects.html",{"projects":projects,'directions':DIRECTIONS, "title":"Проекты ассоциации","min_index":min_index,"max_index":max_index,"last_page":last_page})

def one_project(request, project_pk=1):
    project = Projects.objects.get(id=project_pk)
    other = Projects.objects.exclude(id=project_pk).order_by('?')[:5]
    images = ProjectsImages.objects.filter(project_id=project_pk)
    return render(request,"project.html",{"project":project, "other":other, "images":images,"title": project.title})

def center_projects(request, center_pk, page=1):
    projects_list = Projects.objects.filter(center_id=center_pk,published=True).order_by('title')
    
    paginator = Paginator(projects_list,12)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    
    index = projects.number
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
        
    return render(request,"center_projects.html",{"projects":projects,"title":"Проекты ассоциации", "center":center_pk,"min_index":min_index,"max_index":max_index,"last_page":last_page})

def join(request):

    regions = [(region.key, region.title) for region in Regions.objects.all()]

    if request.POST:
        form = FormCaptcha(request.POST)

        if form.is_valid():
            for obj in regions:
                if obj[0] == request.POST['region']:
                    region = obj[1]
                    break
            organisation = request.POST['organisation']
            org_form = request.POST['org_form']
            description = request.POST['description']
            activities = request.POST['activities']
            experience = request.POST['experience']
            ogrn = request.POST['ogrn']
            volunteers = request.POST['volunteers']
    
            body = "Регион: {} \n" \
                    "Название оранизации: {} \n" \
                    "Организационно-правовая форма юридического лица: {} \n" \
                    "Краткая информация об организации: {} \n" \
                    "Основные направления деятельности: {} \n" \
                    "Опыт участия в волонтерских федеральных проектах и программах: {} \n" \
                    "Номер ОГРН: {} \n" \
                    "Количество волонтеров: {} \n".format(region, organisation, org_form, description, activities, experience,ogrn,volunteers)
            from_email = settings.EMAIL_HOST_USER
            to_email = ['info@avcrf.ru']
            email = EmailMessage(u'Заявка', body , from_email,
                to_email)
    
            if request.FILES:
                for file in request.FILES.getlist('files'):
                    email.attach(file.name, file.read())
    
            if email.send():
                return render(request,"join.html", {"success": "good", "regions": regions,"title":"Присоединиться к Ассоциации","form":form})
            else:
                return render(request,"join.html", {"success": "errors", "regions": regions,"title":"Присоединиться к Ассоциации","form":form})
        else:
                return render(request,"join.html", {"success": "errors", "regions": regions,"title":"Присоединиться к Ассоциации","form":form})
    else:
        form = FormCaptcha()
    
    return render(request,"join.html", {"regions": regions,"title":"Присоединиться к Ассоциации","form":form})

def documents(request):
    doc_files = Documents.objects.all()
    return render(request,"documents.html", {"documents": doc_files,"title":"Документы ассоциации"})

def activities(request):
    return render(request,"activities.html",{"title":"Направления ассоциации"})

def new_activities(request):
    return render(request,"new_activities.html",{"title":"Направления ассоциации"})    

def all_opinions(request):
    opinions = Opinion.objects.all().order_by('-date')
    return render(request, "opinions.html", {"opinions":opinions,"title": "Мнения"})

def opinion(request, opinion_pk=1):

    one_opinion = Opinion.objects.get(id=opinion_pk)
    other = Opinion.objects.exclude(id=opinion_pk).order_by('?')[:5]
    return render(request, "opinion.html", {"opinion":one_opinion, "other":other,"title":"Мнение|"+ one_opinion.name + " "+ one_opinion.fam})

def stories(request):
    history = History.objects.all().order_by('-date')
    return render(request, "stories.html", {'stories':history, "title":"Истории успеха"})

def story(request, story_pk=1):

    one_story = History.objects.get(id=story_pk)
    other = History.objects.exclude(id=story_pk).order_by('?')[:5]
    return render(request, "story.html", {"story":one_story,"other":other,"title":"История успеха|" + one_story.name + " "+ one_story.fam})


def events_projects(request):
    projects_list = Projects.objects.all().filter(center_id=None,published=True)[:6]
    events_list = Events.objects.all().filter(center_id=None,published=True).order_by('-date_event')[:6]
    return render(request, "events_projects.html",{"projects":projects_list, "events":events_list})