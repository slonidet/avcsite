from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.fes_view, name="fes"),
]