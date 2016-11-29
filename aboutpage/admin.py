from django.contrib import admin
from .models import Structure, Contacts


class StructureAdmin(admin.ModelAdmin):
    list_filter = ['struc_soviet']
# Register your models here.

admin.site.register(Structure, StructureAdmin)
admin.site.register(Contacts)