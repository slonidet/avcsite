from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.about, name="about"),
    url(r'^structure/$', views.structure, name="structure"),
    url(r'^partners/$', views.partners, name="partners"),
]