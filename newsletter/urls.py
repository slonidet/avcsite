from django.conf.urls import url
from . import views
from .feeds import NewsRSS

urlpatterns = [
	url(r'^$', views.all_news, name="all_news"),
	
	url(r'^view/$', views.one_new, name="news"),
	url(r'^view/(?P<news_pk>\d+)/$', views.one_new, name="news"),
	
	url(r'^okrug/$', views.okrug_news, name="okrug_news"),
	url(r'^okrug/(?P<okrug_name>\w+)/$', views.okrug_news, name="okrug_news"),
	url(r'^okrug/(?P<okrug_name>\w+)/page/(?P<page>\d+)/$', views.okrug_news, name="okrug_news"),
	
	url(r'^center/(?P<center_pk>\d+)/$', views.center_news, name="center_news"),
	url(r'^center/(?P<center_pk>\d+)/page/(?P<page>\d+)/$', views.center_news, name="center_news"),
	
	url(r'^press_releases/$', views.all_releases, name="press_releases"),
	url(r'^press_releases/view/(?P<release_pk>\d+)/$', views.one_release, name="one_release"),

    url(r'^sitenews/$', NewsRSS() ),
]
