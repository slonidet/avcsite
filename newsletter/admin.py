# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import NewsLetter, NewsImages,PressReleases,PressImages, Rubrics

from regionsmap.models import Centers


class ImagesInline(admin.TabularInline):
    model = NewsImages
    extra = 3

class PressInline(admin.TabularInline):
    model = PressImages
    extra = 3


class PressAdmin(admin.ModelAdmin):
    inlines = [PressInline]

class NewsLetterAdmin(admin.ModelAdmin):
    
    #if not request.user.is_superuser or request.user.username !="chempionat":
        #readonly_fields = ('status',)
    
    inlines = [ImagesInline]
    list_display = ('title', 'date_published','label', 'published')
    
    list_filter = ['published','label']
    
    
    def get_queryset(self, request):
        qs = super(NewsLetterAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.username == "chempionat":
            rubr = Rubrics.objects.get(title="Чемпионат мира")
            return qs.filter(rubric=rubr.pk)
        if request.user.username == "avcuser":
            return qs.filter(label="Пользователь АВЦ")
        center = Centers.objects.get(account=request.user)
        return qs.filter(center_id=center.pk)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ['label']
        self.readonly_fields = []
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('center_id')
        if not request.user.is_superuser:
            self.readonly_fields.append("status_admin")
        if not request.user.username == "chempionat":
            self.readonly_fields.append("status_chempionat")
        
        groups = request.user.groups.values_list('name',flat=True)
            
        
        return super(NewsLetterAdmin, self).get_form(request, obj, **kwargs)
        
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            groups = request.user.groups.values_list('name',flat=True)
            if "Центры" in groups:
                obj.label = "Центр"
                
                center = Centers.objects.get(account=request.user)
                obj.center_id = center
            elif request.user.username == "chempionat":
                obj.rubric = Rubrics.objects.get(title="Чемпионат мира")
                obj.label = "ЧМ"
            elif request.user.username == "avcuser":
                obj.label = "Пользователь АВЦ"
        obj.save()
        
        
    
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(PressReleases, PressAdmin)
admin.site.register(Rubrics)