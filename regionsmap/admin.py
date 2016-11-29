# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from .models import Regions, Centers
# Register your models here.

class CentersInline(admin.StackedInline):
    model = Centers
    extra = 1
    

class RegionsAdmin(admin.ModelAdmin):
    inlines = [CentersInline]
    
class CentersAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(CentersAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            self.exclude=['account', 'source']
        if request.user.is_superuser:
            return qs
        groups = request.user.groups.values_list('name',flat=True)
        if User.objects.filter(pk=request.user.id, groups__name="Центры").exists():
            return qs.filter(account=request.user)
# Register your models here.
admin.site.register(Regions, RegionsAdmin)
admin.site.register(Centers, CentersAdmin)