from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.all_events, name="all_events"),
	url(r'^test/$', views.all_events, name="test_events"),
	url(r'^page/(\d+)/$', views.all_events, name="all_events"),
	url(r'^view/(?P<event_pk>\d+)/$', views.one_event, name="event"),
	url(r'^okrug/(?P<okrug_name>\w+)/$', views.okrug_events, name="okrug_events"),
	url(r'^okrug/(?P<okrug_name>\w+)/page/(?P<page>\d+)/$', views.okrug_events, name="okrug_events"),
	url(r'^center/(?P<center_pk>\d+)/$', views.center_events, name="center_events"),
	url(r'^center/(?P<center_pk>\d+)/page/(?P<page>\d+)/$', views.center_events, name="center_events"),
]