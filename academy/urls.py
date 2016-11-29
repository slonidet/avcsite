from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.academy, name="academy"),
    url(r'^write/$', views.write ),
]