# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from regionsmap.models import Regions

class AcademyForm(forms.Form):
    
    regions_objects = Regions.objects.all()
    regions = []
    
    for region in regions_objects:
        regions.append((region.key, region.title))
    
    region = forms.ChoiceField(choices=regions, label=u"Регион", label_suffix="")
    name = forms.CharField(label=u"Ф.И.О", label_suffix="",widget=forms.TextInput(attrs={'required': 'True'}))
    webinar = forms.CharField(label=u"Участником какого вебинара Вы являетесь?", label_suffix="",required=False)
    idea = forms.CharField(label=u"Ваши идеи и предложения", widget=forms.Textarea(attrs={'required': 'True'}))
