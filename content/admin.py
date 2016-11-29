# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Opinion, Partners, History, Slider, Projects, ProjectsImages, Documents, VideoHomePage
from regionsmap.models import Centers
# Register your models here.

class ImagesInline(admin.TabularInline):
    model = ProjectsImages
    extra = 3
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    
    list_display = ('title','label','published')
    list_filter = ['published','label']
    
    def get_queryset(self, request):
        qs = super(ProjectsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        center = Centers.objects.get(account=request.user)
        return qs.filter(center_id=center.pk)
    
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ["label"]
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('center_id')
        return super(ProjectsAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            groups = request.user.groups.values_list('name',flat=True)
            if "Центры" in groups:
                obj.label = "Центр"
                center = Centers.objects.get(account=request.user)
                obj.center_id = center
            elif request.user.username == "chempionat":
                obj.label = "ЧМ"
        obj.save()
    

admin.site.register(Opinion)
admin.site.register(Partners)
admin.site.register(History)
admin.site.register(Slider)
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(Documents)
admin.site.register(VideoHomePage)