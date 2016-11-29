from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.media, name="media"),
	url(r'^photos/(?P<album_pk>\d+)', views.photo_view, name="photo"),
    url(r'^video/(?P<video_pk>\d+)', views.video_view, name="video"),
]