from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.centers, name="centers"),
	url(r'^page/(\d+)/$', views.centers, name="centers_page"),
	url(r'view/(?P<center_pk>\d+)/$', views.center, name="center"),
	#url(r'^okrug/$', views.okrug_news, name="okrug_news"),
	#url(r'okrug/(?P<okrug_name>\w+)/$', views.okrug_news, name="okrug_news"),
	#url(r'^press_releases/$', views.press_releases, name="press_releases"),

]
