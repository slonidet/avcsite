# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Events, EventsImages, EventsDocuments
from regionsmap.models import Centers
# Register your models here.

class ImagesInline(admin.TabularInline):
    model = EventsImages
    extra = 3
    
class DocumentsInline(admin.TabularInline):
    model = EventsDocuments
    extra = 3

class EventsAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, DocumentsInline ]
    list_display = ('title', 'date_event', 'label','published')
    list_filter = ['published','label']
    
    
    def get_queryset(self, request):
        qs = super(EventsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        center = Centers.objects.get(account=request.user)
        return qs.filter(center_id=center.pk)
    
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ["label"]
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('center_id')
        return super(EventsAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            groups = request.user.groups.values_list('name',flat=True)
            if User.objects.filter(pk=request.user.id, groups__name="Центры").exists():
                obj.label = "Центр"
                
                center = Centers.objects.get(account=request.user)
                obj.center_id = center
            elif request.user.username == "chempionat":
                obj.label = "ЧМ"
        obj.save()

    
    

admin.site.register(Events, EventsAdmin)