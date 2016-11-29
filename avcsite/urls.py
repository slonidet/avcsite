"""avcsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from homepage import views as homeviews
from aboutpage import views as otherviews
from content import views as content_views
from mediacontent import views as media_views


from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #url(r'^search/', include('haystack.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', homeviews.homepage, name='home'),
    url(r'^search/', homeviews.search, name='search'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^news/', include('newsletter.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^about/', include('aboutpage.urls')),
    url(r'^develop/', content_views.develop, name="develop"),
    url(r'^join/', content_views.join, name="join"),
    url(r'^documents/', content_views.documents, name="documents"),
    url(r'^activities/', content_views.activities, name="activities"),
    url(r'^test_activities/', content_views.new_activities),
    
    url(r'^write/', content_views.write, name="write"),
    url(r'^media/', include('mediacontent.urls')),
    url(r'^contacts/', otherviews.contacts, name="contacts" ),
    url(r'^centers/', include('regionsmap.urls') ),
    
    url(r'^academy/', include('academy.urls') ),
    
    url(r'^fes/', include('fes.urls')),
    
    
    url(r'^events_and_projects/', content_views.events_projects, name="events_projects"),
    url(r'^projects/$', content_views.all_projects, name="projects"),
    url(r'^projects/view/(?P<project_pk>\d+)/$', content_views.one_project, name="project"),
    url(r'^projects/page/(\d+)/$', content_views.all_projects, name="projects_page"),
    url(r'^projects/center/(?P<center_pk>\d+)/$', content_views.center_projects, name="center_projects"),
    url(r'^projects/center/(?P<center_pk>\d+)/page/(?P<page>\d+)/$', content_views.center_projects, name="center_projects"),

    url(r'^opinions/$', content_views.all_opinions, name="opinions"),
    url(r'^opinions/view/(?P<opinion_pk>\d+)/$', content_views.opinion, name="opinion"),


    url(r'^stories/$', content_views.stories, name="stories"),
    url(r'^stories/view/(?P<story_pk>\d+)/$', content_views.story, name="story"),
    
    
]
