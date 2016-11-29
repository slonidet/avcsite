from django.shortcuts import render
from newsletter.models import NewsLetter
from content.models import Opinion, Partners, Slider, History, VideoHomePage
from regionsmap.models import Regions, Centers
from events.models import Events

# Create your views here.


def homepage(request):
    images = Slider.objects.all()
    news = NewsLetter.objects.filter(published=True, center_id=None).order_by('-date_published')[:6]
    events = Events.objects.filter(published=True, center_id=None).order_by('-date_event')[:6]
    opinions = Opinion.objects.order_by('?')[:3]
    history = History.objects.order_by('?')[:3]
    partners = Partners.objects.order_by('position')
    regions = Regions.objects.order_by('title')
    centers = Centers.objects.order_by('region_id')
    video = VideoHomePage.objects.order_by('-date_add')[:1]

    return render(request,"homepage.html", {"news": news, "opinions": opinions,
        "partners": partners, 'images': images, 'regions':regions, "centers": centers,
        "events":events, "history":history ,"video": video})

def search(request):
    return render(request,"search.html")
