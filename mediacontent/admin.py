from django.contrib import admin
from .models import Album, Video, AlbumPhoto
# Register your models here.

class ImagesInline(admin.TabularInline):
    model = AlbumPhoto
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

admin.site.register(Album,AlbumAdmin)
admin.site.register(Video)